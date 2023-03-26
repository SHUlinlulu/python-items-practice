"""
测试Python中的函数的使用
"""

#
# def max_value(i, j):
#     """
#     求取两个给定值i, j中较大的那个  # 描述函数功能
#     :param i: 参数值i
#     :param j: 参数值j
#     :return: 较大的那个值
#     """
#     return i if i > j else j
#
#
# a = input("Enter a = ")
# b = input("Enter b = ")
# max_ab = max_value(a, b)
# print(f"{a},{b}中较大的是{max_ab}")


def demo(param=[]):
    print("param的值：", param)
    param.append(1)


demo()  # return:[]
demo()  # return:[1]----这显然不是我们所需要的


# 改进
def demo(param=None):
    if param is None:
        param = []
    print("param的值：", param)
    param.append(1)


demo()  # return:[]
demo()  # return:[]

