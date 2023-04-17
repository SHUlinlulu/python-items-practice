"""
    目标：使用第三方库requests简化python自带模块urllib的web操作,进而简化爬虫代码
    安装：pip install requests
    国内镜像安装：
        1.百度搜索 “pip清华源”
        2.采用清华镜像下载格式pip指定模块(尽量采用临时 -i)
    Attentions: GET and POST
    GET请求方式：一般用于查询--显式请求
    POST请求方式：一般针对页面进行了修改变动
    本质，没撒子影响！
"""
import requests

url = "https://www.sogou.com/web?query=胡歌"

headers = {  # 设置代理--访问的浏览器，假装以浏览器形式访问该网站----针对一些网站的小小反爬取措施
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36 Edg/112.0.1722.48"
}

response = requests.get(url=url, headers=headers)  # 发起请求

print(response.text)  # 获得返回的页面源代码--html
print(response)

# 简言之。requests相当于对于urllib作了一个简化的操作
