import jmcomic
import os
import time
import random
import yaml
from PIL import Image
import requests

# 设置随机延迟
def random_delay(min_delay=1, max_delay=3):
    time.sleep(random.uniform(min_delay, max_delay))

# 设置代理 IP 池
PROXY_POOL = [
    "http://proxy1_ip:port",
    "http://proxy2_ip:port",
    # 添加更多代理 IP
]

# 获取随机代理
def get_random_proxy():
    return random.choice(PROXY_POOL)

# 下载漫画并重试
def download_with_retry(album_id, option, max_retries=5):
    for attempt in range(max_retries):
        try:
            # 设置随机代理
            proxy = get_random_proxy()
            print(f"使用代理: {proxy}")

            # 设置 requests 的代理
            session = requests.Session()
            session.proxies = {"http": proxy, "https": proxy}

            # 将 session 传递给 jmcomic
            option.set_session(session)

            # 下载漫画
            jmcomic.download_album(album_id, option)
            break  # 成功则退出重试
        except Exception as e:
            print(f"下载失败（尝试 {attempt + 1}/{max_retries}）: {e}")
            if attempt < max_retries - 1:
                random_delay()  # 随机延迟
            else:
                print("下载失败，已达到最大重试次数")

# 将图片转换为 PDF
def all2PDF(input_folder, pdfpath, pdfname):
    start_time = time.time()
    paht = input_folder
    zimulu = []  # 子目录（里面为image）
    image = []  # 子目录图集
    sources = []  # pdf格式的图

    with os.scandir(paht) as entries:
        for entry in entries:
            if entry.is_dir():
                zimulu.append(int(entry.name))
    # 对数字进行排序
    zimulu.sort()

    for i in zimulu:
        with os.scandir(os.path.join(paht, str(i))) as entries:
            for entry in entries:
                if entry.is_dir():
                    print("这一级不应该有子目录")
                if entry.is_file():
                    image.append(os.path.join(paht, str(i), entry.name))

    if len(image) > 0 and ("jpg" in image[0] or "jpeg" in image[0]):
        output = Image.open(image[0])
        image.pop(0)
    else:
        print("未找到图片文件")
        return

    for file in image:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            try:
                img_file = Image.open(file)
                if img_file.mode != "RGB":
                    img_file = img_file.convert("RGB")
                sources.append(img_file)
            except Exception as e:
                print(f"无法打开图片文件 {file}: {e}")

    pdf_file_path = os.path.join(pdfpath, pdfname)
    if not pdf_file_path.endswith(".pdf"):
        pdf_file_path += ".pdf"

    try:
        output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)
    except Exception as e:
        print(f"保存 PDF 失败: {e}")

    end_time = time.time()
    run_time = end_time - start_time
    print("运行时间：%3.2f 秒" % run_time)


if __name__ == "__main__":
    # 自定义设置：
    config = "/Users/casomthesus/PycharmProjects/pythonProject/Config/config.yml"
    loadConfig = jmcomic.JmOption.from_file(config)

    # 如果需要下载，则取消以下注释
    manhua = ['146417']
    for id in manhua:
        download_with_retry(id, loadConfig)

    with open(config, "r", encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        path = data["dir_rule"]["base_dir"]

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                pdf_path = os.path.join(path, entry.name + ".pdf")
                if os.path.exists(pdf_path):
                    print(f"文件：《{entry.name}》 已存在，跳过")
                    continue
                else:
                    print(f"开始转换：{entry.name}")
                    all2PDF(os.path.join(path, entry.name), path, entry.name)
