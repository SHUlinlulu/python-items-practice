"""
    测试使用代理访问指定网站
"""
import requests

url = "https://www.17k.com/"
# 代理---ip:port,一般选择“透明”类型,可用
proxies = {
    "https": "121.41.48.76:3128"  # 有的版本"https"/"http"的value需要写成"https://121.41.48.76:3128"
}
resp = requests.get(url=url, proxies=proxies)  # 使用代理速度明显变慢
resp.encoding = "utf-8"
print(resp.text)
