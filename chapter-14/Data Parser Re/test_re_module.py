"""
    测试使用Python中的re module
"""
# import packages
import re

# # 1. findall->list,匹配给定字符串中所有符合条件的匹配项---列表的效率并不高，若是匹配的str很长，不推荐也不常用
# match_list = re.findall(r"\d+", "我的电话号码是10086，我女朋友的电话号码是10010。")
# print(match_list)

# # 2. finditer->iterator,匹配字符串中所有的内容[返回值是一个迭代器对象],从迭代器拿到内容需要.group()获取
# match_iter = re.finditer(r"\d+", "我的电话号码是10086，我女朋友的电话号码是10010。")
# for i in match_iter:  # 迭代器的效率肯定比列表要高得多
#     print(i)
#     print(i.group())

# # 3. search进行全文检索，返回第一个满足条件的match对象。拿到数据，需要.group()
# match_object = re.search(r"\d+", "我的电话号码是10086，我女朋友的电话号码是10010。")
# print(match_object.group())

# # 4. match进行从头匹配,相当于patterns中添加了一个“^”，即匹配开始符，开头匹配上就返回match对象，否则None
# result = re.match(r"\d+", "我的电话号码是10086，我的女朋友电话号码是10010。")
# print(result.group())
# # 'NoneType' object has no attribute 'group',如此报错,仅需找到报错行,必定是 "."前内容为None

"""
    re.compile(patterns, flags)----预加载正则表达式
    目的：后续写的复杂的正则表达式可能需要反复的使用
    re.finditer(string, flags)
"""
# pattern = re.compile(r"\d+")  # 返回的就是一个Pattern对象
# match_iter = pattern.finditer("我的电话号码是10086，我的女朋友电话号码是10010。")
# for i in match_iter:
#     print(i.group())
#
# match = pattern.search("哈哈哈哈，我就不行你不还我1000000")
# print(match.group())

"""
    提取匹配正则表达式后的内容：(?P<名字>内容)
"""
string = """
    <div class='jay'><span id=1>郭麒麟</span></div>
    <div class='jj'><span id=2>宋轶</span></div>
    <div class='jo'><span id=3>大聪明</span></div>
    <div class='jean'><span id=4>范思哲</span></div>
    <div class='jak'><span id=5>郭永年</span></div>
"""
# re.S:--属于flags内容，目的：就是让.能够匹配换行符\n，防止匹配过程中断行----即连续匹配一个，继续从此匹配另一个
# (?P<分组名字>正则) 可以单独从正则匹配的内容进一步提取数据
pattern = re.compile(r"<div class='.*?'><span id=(?P<id>\d+)>(?P<name>.*?)</span></div>", re.S)
res_iter = pattern.finditer(string)
for i in res_iter:  # i:match object
    # print(i.group())  # 获得match对象内容.group()即可
    print(i.group("id"), end=" ")  # 输出分组名为id的内容
    print(i.group("name"))
