"""
    使用Re模块对数据文本进行解析提取想要的数据
    举例：拿到豆瓣网Top250的电影的名称、图片链接、上映年份、评分和评价人数
"""
import csv

# 1. 拿到数据页面源码
# 2. 对页面信息进行提取，获得想要的信息
import requests
import re

url = "https://movie.douban.com/top250"
# 配置headers参数---伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
# 配置params---为了动态的获取所有数据Top250
range_page = 10
pages_start = list()
for i in range(0, 250, 25):
    pages_start.append(i)
start = pages_start[0]
params = {
    "start": f"{start}"
}
response = requests.get(url=url, headers=headers, params=params)  # 发起请求获得响应
source_code = response.text  # 访问Response类的response对象的计算性质的属性——页面源码
# print(source_code)  # 打印->显示为空，说明需要配置headers参数，伪装浏览器

# 2. Re 模块解析数据
# 预加载正则表达式
# re.S: flags位,使得 "."能够匹配换行符
pattern = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<movie_name>.*?)</span>'
                     r'.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<number>\d+)人评价</span>', re.S)

results = pattern.finditer(source_code)
csvfile = open("movie_top.csv", mode='w', encoding="utf-8")
csvwriter = csv.writer(csvfile)
for i in results:
    # print(i.group("movie_name"))  # 电影名称
    # print(i.group("year").strip())  # 上映时间
    # print(i.group("score"))  # 电影评分
    # print(i.group("number"))  # 评价人数
    dict_data = i.groupdict()
    dict_data['year'] = dict_data['year'].strip()
    # print(dict_data)
    # 将数据写到csv文件中去，csv文件内容特点：电影名称,上映时间,电影评分,评价人数——即：","将每行数据隔开
    csvwriter.writerow(dict_data.values())

csvfile.close()
response.close()
print("over!!!!")






