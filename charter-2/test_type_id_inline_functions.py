"""
测试使用Python中的内置函数type(parameter)->变量/表达式类型；  id(parameter)->变量的内存地址
"""


def sum_integer(a, b):
    return a + b


class Student:
    name = "林露露",
    gender = True  # True represents '男' while False represents '女'
    age = 24

    def __init__(self, name: str, gender: bool, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.name}\t{self.gender}\t{self.age}"


print(f"type of integer is {type(16)}")  # type(parameter)->Object
student = Student("林露露", True, 23)
print(f"memory address of student is {id(student)}")  # id(parameter)->int
if student.gender:
    gender1 = '男'
else:
    gender1 = '女'
print(f"{student.name}性别是{gender1}，今年{student.age}岁")
