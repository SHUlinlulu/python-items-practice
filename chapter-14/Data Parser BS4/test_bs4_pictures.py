"""
    使用bs4中的BeautifulSoup解析爬取的美女图片
    案例：
    爬取网址：https://www.umei.cc/meinvtupian/
"""
import requests
from bs4 import BeautifulSoup

# 获得domain页面源代码
url = "https://www.umei.cc/meinvtupian/"
resp_main = requests.get(url)
resp_main.encoding = 'utf-8'
page_main = resp_main.text  # type: str

# 将页面源代码交给BeautifulSoup,得到bs对象
bs_page_main = BeautifulSoup(page_main, "html.parser")  # 指定html页面解析器
bs_Clbc_top = bs_page_main.find("div", class_="Clbc_top")
bs_resultsSet_li = bs_Clbc_top.find_all("li")
dic_pic_link = {}
sub_links = list()
for li in bs_resultsSet_li:
    bs_p = li.find("p")
    href = bs_p.find("a").get("href")
    sub_links.append(url + href.strip('/meinvtupian') + 'tm')
# 处理子页面
for sub_link in sub_links:
    sub_resp = requests.get(sub_link)
    sub_resp.encoding = "utf-8"  # 防止乱码
    sub_page = sub_resp.text  # 得到子页面源代码
    # 交给BeautifulSoup处理
    bs_sub_page = BeautifulSoup(sub_page, "html.parser")
    bs_sub_div = bs_sub_page.find("div", attrs={"class": "big-pic"})
    try:
        image_src = bs_sub_div.find("img").get("src")
    except:
        continue
    image_name = image_src.split("/")[-1]
    image_resp = requests.get(image_src)
    image_content = image_resp.content
    with open("beauty/"+image_name, "wb") as image_file:
        image_file.write(image_content)
    image_resp.close()
    sub_resp.close()
resp_main.close()  # 关闭连接
print("over!!!!!")


