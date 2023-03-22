"""
测试list的内置方法
"""
# my_list = ["林露露", "张三", 24, "itheima", 125.2920, (23, 24, '许思')]
# for index, value in enumerate(my_list):
#     print(index, value)
import random
rand_num = [random.randint(10, 101) for i in range(10)]
print(rand_num)
