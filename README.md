# Better-JMComic-Crawler
基于避免被网站屏蔽的考虑，添加了请求间隔和随机代理IP的代码，优化了原代码性能。
# 感谢以下项目
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=hect0x7&repo=JMComic-Crawler-Python)]([https://github.com/tonquer/JMComic-qt](https://github.com/hect0x7/JMComic-Crawler-Python)https://github.com/hect0x7/JMComic-Crawler-Python)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=salikx&repo=image2pdf)](https://github.com/salikx/image2pdf)
# 功能介绍
将jmcomic里车号对应的本子下载并自动转化为pdf格式。
# 用法说明
1.在python编译器里下载如下三个必需库：
  ```shell
  pip install jmcomic -i https://pypi.org/project --upgrade
  pip install pillow
  pip install pyyaml 
  ```
2.main.py在运行前需要取消掉如下三行注释，并配置相应config路径：
```shell
manhua = ['146417']  
for id in manhua:
  jmcomic.download_album(id,loadConfig)
```
（需要取消掉的注释，main.py中已事先取消注释，可用于测试代码运行）

3.上一条中的manhua列表中可填写多个需要下载的本子车号，格式按['114514','350234']，如此类推。
# 特别注意
1.由于下载大量图片时，批量转换会预先将图片写入内存中，因此本子超过150话以上时，如果电脑内存小于32G，尽量避免尝试。
2.使用前在config文件中按照电脑配置修改最后的batch_count参数。


  
