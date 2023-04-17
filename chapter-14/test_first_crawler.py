# 爬虫：通过编写程序模拟浏览器来获取网络上的数据
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取资源或内容

# 1.import packages
from urllib.request import urlopen
# 2.打开网址
response = urlopen('https://www.baidu.com')  # 获取的相应response中包含许多东西，如：响应码/响应头部信息...
with open('baidu.html', mode='w') as file:
    file.write(response.read().decode("utf-8"))
    # response.read()获取的数据信息编码为字节码---->需要解码（utf-8）---->str
print("over!")
response.close()
"""
Web请求过程刨析：----进入网络页面，‘检查或F12’，查看‘network’--回车刷新数据
    服务器端渲染：baidu.com为例，输入关键字信息，返回的关键字信息与html页面嵌在一起，即数据在Html页面中----后续需要提取
    
    客户端渲染：豆瓣电影网为例，第一次返回的是Html骨架，数据在后续的请求中以规整的形式返回(即发起了新的数据请求----需要细心寻找)
启示：在抓取数据的时候，数据不一定是一次全返回的，需要挨个请求仔细寻找
"""