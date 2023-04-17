"""
    测试使用requests模块中的post请求方式处理百度翻译中的英译汉单词翻译抓包数据
    需求：访问fanyi.baidu.com，输入英文返回中文
    注意事项：在浏览器 “检查” 过程中，打开或在百度翻译中输入内容前需要将输入法调成英文输入法，否则是看不到sug这个字段请求页面的
    Form Data
"""
import requests

url = "https://fanyi.baidu.com/sug"
s = input("please input the word you want to translate:")
data = {  # 在目前的浏览器的负载里可以看到需要传递的参数--dic
    'kw': s
}
# 发送post请求，发送的数据必须放在字典(dict)中，通过post方法中的data参数进行传递
response = requests.post(url=url, data=data)
print(response.json())  # 将服务器返回数据解析成json格式--> dict(python)
for element in response.json()['data']:
    print(element['k'], f":{element['v']}")

response.close()  # 关闭，否则keep-alive占用容易堵塞
"""
    启发：可以根据此案例开发一个可视化接口专门做百度翻译的英译汉单词接口小程序
"""
