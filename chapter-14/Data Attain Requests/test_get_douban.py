"""
    使用requests模块的案例3--爬取豆瓣网站的数据
    豆瓣网：典型的客户端渲染，即数据不是简单的塞在HTML中，而是需要寻找的，比如：豆瓣的 ‘FETCH/XHR’选项的请求文件
    GET:参数一般浏览器都给你整理好了
    Query String Parameters --负载里可看到
"""
import requests

url = "https://movie.douban.com/j/chart/top_list"

# 若参数比较长，则对其进行封装
# 快捷键--选中内容，双击鼠标，则加上了双引号
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
# 设置headers参数
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 发起请求
response = requests.get(url=url, params=params, headers=headers)
# print(response.request.url)  # 验证请求地址是否拼接正确
# print(response.text)  # 在未加headers参数之前打印获得的结果是空白的，说明该网址采取了一定的反爬措施，最常见User-Agent
# print(response.request.headers)  # 打印而得到User-Agent显然不是浏览器方式请求，需要设置User-Agent参数
print(response.json())  # json格式输出相应的内容

# 警告：莫忘记关闭response
response.close()  # 否则很容易造成堵塞

"""
    启发：下拉页面时数据会进行更新，而查看对应页面，也只是发现传递的参数start的数值发生了改变
    因此，如果要爬取很多条数据，就只需要动态的改变start的值
"""
