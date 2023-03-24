# """
# 测试使用Python提供的re模块---Regular Expression(正则表达式)
# """
# import re
# pattern = r'linlulu\w*'
# string_1 = "Linlulu is a graduate studying in Shanghai University!His name" \
#            "is Linlulu, and his email is linlulu@shu.edu.cn"
# # match = re.match(pattern, string_1, re.I)
# # print(match)
# # print(match.group())
# # print(match.span())
# # print(match.string)
# match = re.search(pattern, string_1)
# print(match)
# import re
# pattern = r'mr_\w+'
# string = "Mr_show MR_SHOP"
# match = re.findall(pattern, string, re.I)
# print(match)

# import re
# pattern = r'([1-9]{1,3}(.[0-9]{1,3}){3})'  # 匹配IP地址,不包含0.0.0.0
# string = '127.0.0.1 192.168.37.252'
# match = re.findall(pattern, string)  # type:list[str]
# print(match)

# import re
# pattern = r'1[34578]\d{9}'
# string = '中奖号码是：628929 联系电话为：13628929191'
# result = re.sub(pattern, '1xxxxxxxxxx', string)  # 替换字符串
# print(result)

import re
pattern = r'[?|&]'  # 定义分隔符
url = 'https://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern, url)  # 分割字符串
print(result)


