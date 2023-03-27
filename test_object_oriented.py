# """
#  测试Python中类的定义与使用
# """
#
#
# class Person:  # 类名---规范(首字母大写--'驼峰命名法')
#     """
#     类的帮助信息----比如：功能说明、属性方法说明等
#     """
#     def __init__(self, name: str, age: int, gender: str, address: str):
#         # 通过定义属性在方法__init__()中----实例属性
#         self.name = name  # 姓名
#         self.age = age  # 年龄
#         self.gender = gender  # 性别
#         self.__address = address  # 家庭住址----private属性
#
#     def __str__(self):
#         return f"{self.name}, {self.age}, {self.gender}"
#
#     @property
#     def printInfo(self):  # 定义类Person的计算特性的属性----printInfo
#         print(f"姓名：{self.name}\t性别：{self.gender}\t年龄：{self.age}")
#
#     @property
#     def address(self):
#         return self.__address
#
#
# person = Person("林露露", 24, "男", "上海市嘉定区嘉定镇街道城中路20号")
# person.printInfo  # 访问类Person的计算特性的属性----printInfo
# print(person.address)


class TVShow:
    list_film = ["红海行动", "绿里奇迹", "绝命毒师", "海上钢琴家", "钢琴家", "触不可及"]

    def __init__(self, show):
        self.__show = show

    @property
    def show(self):  # 定义show方法
        return self.__show  # 返回私有属性的值

    @show.setter  # 设置setter方法，使得属性值可以修改
    def show(self, value):
        if value in TVShow.list_film:
            self.__show = f"您选择了{value},稍后将播放..."  # 返回修改后的属性值
        else:
            self.__show = f"不好意思，您点播的电影不在播放列表中，请重新选择！！"


tv_show = TVShow("触不可及")
print(f"正在播放：{tv_show.show}")  # 直接访问计算特性属性----show
print(f"++++++++++您可以从{tv_show.list_film}中选择您要播放的电影！！+++++++++")
tv_show.show = "红海行动"  # 修改属性值
print(tv_show.show)  # 获取属性值

