"""
    测试使用lambda表达式，体会python中匿名函数的使用
    案例描述：
        人民币转美元，汇率1:6.42
"""
import random
# 使用列表表达式创建10个1000~100000的随机整数组成的列表
ren_min_bi = [random.randint(1000, 100000) for x in range(10)]
result = lambda x: x * 6.42
print(f"人民币：{ren_min_bi}")
dollars = []
for item in ren_min_bi:
    dollars.append(result(x=item))  # 关键字传参

print("美元：", end=" ")
for i in dollars:
    print("{:.2f}".format(i), end=" ")



