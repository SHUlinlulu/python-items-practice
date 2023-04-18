"""
    练习使用python中的requests module获取页面源代码; re module 解析页面
    案例：抓取https://www.dytt.com中一栏电影的相关字段信息
    提升：
        1. 首先获得是主页面源码，再根据主页面源码提取子页面链接封装成一个list
        2. 迭代访问list，依次访问子页面，获得子页面源码，根据子页面提取想要的字段信息
"""
import csv

import requests
import re

# 获得首页面信息
url = "https://www.dytt89.com/"
headers = {  # 不管页面访问的网站是否有反爬措施，伪装成浏览器总不会有错
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
main_response = requests.get(url=url, headers=headers)
main_response.encoding = 'gb2312'  # 设置请求响应编码格式设置为gb2312 or gbk ----都是国标码
main_page = main_response.text  # type: str
# 解析main page
# 预加载正则表达式,re.S使得.能够匹配换行符\n
main_pattern = re.compile(r'2023必看热片.*?<ul>(?P<movie_li>.*?)</ul>', re.S)
main_results = main_pattern.search(main_page)
main_li_str = main_results.group("movie_li").strip()  # type: str
link_pattern = re.compile(r"<li><a href='(?P<sub_link>.*?)' title", re.S)
link_results = link_pattern.finditer(main_li_str)
sub_page_links = list()
for i in link_results:
    # 拼接获得子页面完整链接
    sub_page_link = "https://www.dytt89.com/" + i.group('sub_link').strip('/')
    sub_page_links.append(sub_page_link)
# 访问子页面获取子页面信息
csv_file = open("dytt_movies.csv", mode='w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
for sub_link in sub_page_links:
    sub_response = requests.get(sub_link, headers=headers)
    sub_response.encoding = 'gb2312'
    sub_page = sub_response.text  # 子页面源码内容
    # 提取子页面内容
    sub_pattern = re.compile(r'◎片　　名　(?P<name>.*?)<br />◎年　　代　(?P<year>.*?)<br />.*?'
                             r'◎类　　别　(?P<type>.*?)<br />.*?◎豆瓣评分　(?P<score>.*?).*?'
                             r'<ul>		<li><a href="(?P<link>.*?)">', re.S)
    sub_result = sub_pattern.search(sub_page)  # type: Match
    csv_writer.writerow(sub_result.groupdict().values())  # 将获得的数据写到文件dytt_movies.csv中
    sub_response.close()  # 用完则关闭response连接，否则造成堵塞
csv_file.close()  # 关闭文件
main_response.close()







