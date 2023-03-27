"""
    观察Python中的在子类对象中调用父类的__init__()方法
"""
# define a Person class


class Person:  # "驼峰命名风格"

    def __init__(self, name: str, gender: str, age: int, address: str):
        self.name = name  # 姓名
        self.gender = gender  # 性别
        self.age = age  # 年龄
        self.__address = address  # 地址--private

    def __str__(self):
        return f"Name: {self.name}\tGender: {self.gender}\t Age: {self.age}"

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, author):
        if author == "林露露":
            self.__address = "安徽省阜阳市临泉县"
        else:
            print("不好意思，输入姓名权限不对，不能修改地址！！！")

    def show(self):
        print(self.__str__(), end=" ")
        print(f"Address: {self.address}")  # 获取address属性值


class Student(Person):  # Student class inherit from Person class
    def __init__(self, stu_num: int, stu_major: str, stu_name: str, stu_gender: str, stu_age: int, stu_address: str):
        self.__stu_num = stu_num  # 学号--private
        self.__stu_major = stu_major  # 专业--private
        super().__init__(stu_name, stu_gender, stu_age, stu_address)

    @property
    def stu_num(self):  # 通过装饰器(decorator)将方法变为计算特性的属性
        return self.__stu_num

    @property
    def stu_major(self):
        return self.__stu_major

    # 重写show方法
    def show(self):
        print(f"Stu_Num: {self.stu_num}\tStu_Major: {self.stu_major}\t", end=" ")
        super().show()


person = Person("王可可", "女", 23, "安徽省阜阳市临泉县")
print(f"{person.name}的居住地址为：", person.address)
person.address = input("请输入操作人员：")
print(person.address)
person.show()

student = Student(22721625, "软件工程", "林露露", "男", 24, "上海市嘉定区嘉定镇街道城中路20号")
print(f"{student.name}的学号为: {student.stu_num}")
print(f"{student.name}的专业为: {student.stu_major}")
student.show()







