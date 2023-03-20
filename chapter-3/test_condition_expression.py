"""
在程序设计时，经产需要根据表达式的值，进而为变量或表达式进行赋值
    ---Python提供了一种简便的写法，可依简化代码量
"""
# 原始写法
import random

# 求一个整数的绝对值
abs_num = 0
num = random.randint(-100, 101)  # 随机产生-100~100的整数
if num > 0:
    abs_num = num
else:
    abs_num = -num

print(f"{num}的绝对值是:{abs_num}")

# Python提供的使用条件表达式写法---主要就替换 if...else 模块
abs_num_exp = 0
'''
一般格式：variable_ret = 左值 if expression else 右值
规则：
    若expression->True,将左值赋给variable_ret
    反之，将右值赋给variable_ret
'''
abs_num_exp = num if num > 0 else -num
print(f"采用条件表达式后，{num}的绝对值计算为:{abs_num_exp}")



