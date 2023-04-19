"""
    使用xpath解析”优美图库“上抓取的页面
"""
import requests
from lxml import etree
# 1.获得页面源码
url = "https://www.umei.cc/meinvtupian/siwameinv/"
resp = requests.get(url=url)
resp.encoding = "utf-8"
page_text = resp.text  # type: str

# 2.使用etree module 中的xpath解析
tree = etree.HTML(page_text)
image_list = tree.xpath("//*[@id='infinite_scroll']/div/div[1]/div/a/img/@data-original")
for link in image_list:
    image_name = link.split("/")[-1]
    link_resp = requests.get(link)
    img_content = link_resp.content
    with open("images/" + image_name, mode='wb') as img_file:
        img_file.write(img_content)
    link_resp.close()
resp.close()
print("all over!!!!!!!!")
