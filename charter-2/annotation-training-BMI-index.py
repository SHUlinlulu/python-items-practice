# coding:utf-8 or coding=utf-8 -----Python 3.10版本已取消
# 中文编码声明注释
"""
    @ 功能:根据身高,体重计算BMI指数
    @ author:林露露
    @ create:2023-3-19
"""
print("""根据身高，体重计算BMI指数""")
# """ contents """前无变量接收值且不用在Python语句中，其"""contents"""才表示多行注释
# ==================== 程序结束 ==================== #
# 输入身高与体重
height = float(input("请输入您的身高(单位m):"))  # input从键盘接收的内容都是字符串
weight = float(input("请输入您的体重(单位kg):"))  # 需要将其转换为所需要数据类型

bmi = weight / (height ** 2)

print(f"您的BMI指数为:{bmi}")
# print("您的BMI指数为: %f", bmi)
print("您的BMI指数为:"+str(bmi))  # print("您的BMI指数为:"+str(bmi))
# Expected type 'str', got 'float' instead

# 判断身材是否合理
if bmi < 18.5:
    print("您的体重过轻~@_@~")
elif 18.5 <= bmi < 24.9:
    print("正常范围，注意保持(-_-)")
elif 24.9 <= bmi < 29.9:
    print("您的体重过重~@_@~")
elif bmi >= 29.9:
    print("肥胖...(@——@)")

# ==================== 程序结束 ==================== #

