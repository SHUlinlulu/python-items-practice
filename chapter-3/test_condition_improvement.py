"""
    "今有物不知其数，三三数之剩二，五五数之余三，七七数之剩二，问几何？"
    今给予汝100次机会，能猜对否？
"""
import random
# initial the condition variable and count
flag = True
count = 0  # 猜测次数
while flag:
    guess_number = random.randint(1, 100)
    count += 1  # 进循环先自增
    if (guess_number % 3 == 2) and (guess_number % 5 == 3) and (guess_number % 7 == 2):
        print(f"问几何？结果是{guess_number}")
        print(f"您是第{count}次猜对的，真幸运！！！！！！！！")
        flag = False
    elif count >= 100:
        print("不好意思，您的竞猜次数用完了，欢迎下次竞猜！！！！！！")
        flag = False



