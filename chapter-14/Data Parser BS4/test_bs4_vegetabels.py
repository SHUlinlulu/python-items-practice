"""
    使用bs4 module中的BeautifulSoup解析抓取的数据
    1.安装bs4  -- pip install [-i xxx] bs4
    2.浏览器输入"长春菜市场网"，爬取该网站发布的每天的菜价 --价格
    抓取的是一个表格；在表中在进一步提取；...
"""
import json

import requests
from bs4 import BeautifulSoup
# 1. 拿到页面源代码
url = "https://www.cccsc.cn/index.php"
# 只需要动态修改page的值，就可以抓取很多数据
for page in range(1, 7):
    params = {
        "app": "search",
        "cate_id": 1,
        "page": f"{page}"
    }
    resp = requests.get(url=url, params=params)
    resp.encoding = 'utf-8'
    page_text = resp.text  # 拿到页面源码

    # 2. 使用bs4对页面进行解析，拿到数据
    # 将页面源码交给BeautifulSoup得到bs对象
    obj = BeautifulSoup(page_text, 'html.parser')  # 指定html解析器
    list_goods = obj.find("div", id="list-goods")
    h2_list = list_goods.find_all("h2")
    # div_list = list_goods.find_all("div", class_="p-price")  # 为了区分属性名与python中的保留字，特在属性后加以下划线
    div_price_list = list_goods.find_all("div", attrs={"class": "p-price"})  # 与上一句等价
    fruit_name_list = list()
    fruit_price_list = list()
    for h2 in h2_list:
        a = h2.find("a")
        fruit_name_list.append(a.text)
    for div in div_price_list:
        price = div.find("span").text
        fruit_price_list.append(price)
    dic_fruits = dict(map(lambda x, y: [x, y], fruit_name_list, fruit_price_list))
    # dic = dict(map(lambda x,y:[x,y],list1,list2))
    json_str = json.dumps(dic_fruits, ensure_ascii=False)  # 少了ensure_ascii，数据\u即中文乱码
    with open("菜价.txt", "a", encoding="utf-8") as json_file:
        json_file.write(json_str)

print("all over!!!!")






