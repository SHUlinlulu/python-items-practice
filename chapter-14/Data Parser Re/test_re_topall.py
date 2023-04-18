"""
    使用requests module获得page_content,使用re module解析page_content得到想要的数据
    案例：爬取douban.com中的top250的数据：电影图片
"""
import requests
import re

# 获得page_content
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
for start in range(0, 250, 25):
    params = {
        "start": f"{start}"
    }
    response = requests.get(url=url, headers=headers, params=params)
    page_content = response.text  # type: str
    # 进行页面解析
    pattern = re.compile(r'<li>.*?<div class="item">.*?<img width="100" alt="(?P<name>.*?)" src="(?P<link>.*?)'
                         r'" class="">', re.S)
    page_results = pattern.finditer(page_content)
    for i in page_results:
        link = i.group("link")  # 获得图片下载链接
        image_resp = requests.get(url=link, headers=headers)  # 伪装浏览器打开图片链接
        image_b = image_resp.content  # 得到图片的字节码字符串
        with open(f"images/{i.group('name')}.jpg", mode='wb') as image_file:
            image_file.write(image_b)

print("over!!!")

