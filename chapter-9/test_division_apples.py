"""
    使用Python异常处理语句try ... except ... 以及向上抛异常 raise语句
"""


def division_apples():
    """
    给指定数目m个小朋友分n个苹果
    :return: None
    """
    n = int(input("请输入苹果数目："))
    m = int(input("请输入小朋友数目："))
    result = n // m  # n整除m
    remains = n - result * m  # remains：剩余苹果数目
    if m > n:
        raise ValueError("要分的苹果数目太少了...")
    else:
        print(f"{m}个小朋友要分苹果{n}个,每个小朋友都分得{result}个苹果，还剩余{remains}个")


if __name__ == '__main__':
    try:
        division_apples()
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)  # e = "要分的苹果数目太少了..."
