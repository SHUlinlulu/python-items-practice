"""
使用if语句的嵌套判断酒驾
描述：酒精含量
    1.小于20mg/100ml----不构成酒驾
    2.大于等于20mg/100ml and 小于等于80mg/100ml----饮酒驾驶
    3.大于80mg/100ml----醉酒驾驶
要求：
    write a python program to judge is one driver is drunk driving and his/her degree
"""
import random
print("\n为了您的健康和他人的安全，严禁酒后开车！\n")
proof = random.randint(0, 101)  # 产生[0,101)随机整数
print(f"测得你的100毫升血液酒精含量:{proof}")
if proof < 20:
    print("\n您还不构成饮酒行为，可以开车，但要注意安全！")
else:
    if proof > 80:
        print("已经达到醉酒驾驶标准，请下车接受处罚！---扣分12分，拘留15天")
    else:
        print("已经达到饮酒驾驶，请出示你的驾照！---扣3分，罚款200元")






