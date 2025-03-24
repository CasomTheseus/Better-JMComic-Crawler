# Better-JMComic-Crawler
基于避免被网站屏蔽的考虑，添加了请求间隔和随机代理IP的代码，优化了原代码性能。
# 感谢以下项目
https://camo.githubusercontent.com/829d6899bdc6924f3123048d91b8eeffde0e72b02b244ead5ba30b192bbefd46/68747470733a2f2f6769746875622d726561646d652d73746174732e76657263656c2e6170702f6170692f70696e2f3f757365726e616d653d68656374307837267265706f3d4a4d436f6d69632d437261776c65722d507974686f6e
https://github.com/salikx/image2pdf
# 功能介绍
将jmcomic里车号对应的本子下载并自动转化为pdf格式。
# 用法说明
1.在python编译器里下载如下三个必需库：
pip install jmcomic -i https://pypi.org/project --upgrade
pip install pillow
pip install pyyaml 
2.main.py在运行前需要取消掉如下三行注释，并配置相应config路径：
manhua = ['350234']  
for id in manhua:
  jmcomic.download_album(id,loadConfig)（需要取消掉的注释，main.py中已事先取消注释，可用于测试代码运行）
3.上一条中的manhua列表中可填写多个需要下载的本子车号，格式按['114514','350234']，如此类推。
# 特别注意
1.由于下载大量图片时，批量转换会预先将图片写入内存中，因此本子超过150话以上时，如果电脑内存小于32G，尽量避免尝试。
2.使用前在config文件中按照电脑配置修改最后的batch_count参数。


  
