"""
    使用Python的标准模块设计实现验证码的生成与验证
"""
import random

if __name__ == '__main__':
    checkcode = ""
    for i in range(4):
        index = random.randint(0, 4)
        if index != i and index + 1 != i:  # chr(__int)->char
            checkcode += chr(random.randint(99, 122))  # 随机生成a-z一个字符
        elif index + 1 == i:
            checkcode += chr(random.randint(65, 90))  # 随机生成A-Z一个字符
        else:
            checkcode += str(random.randint(0, 9))

    print(checkcode)
