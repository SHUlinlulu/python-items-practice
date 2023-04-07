# # """
# #     测试使用GUI界面设计模块wxPython
# # """
# # import wx
# #
# #
# # class App(wx.App):  # 创建一个wx.App的子类App
# #     # 初始化方法
# #     def OnInit(self):
# #         frame = wx.Frame(parent=None, title='Hello wxPython')  # 创建窗口
# #         frame.Show()  # 显示窗口
# #         return True
# #
# #
# # if __name__ == '__main__':
# #     app = App()  # 创建App类的实例对象
# #     app.MainLoop()  # 调用App类的MainLoop()主循环方法
#
#
# """
#     直接使用wx.App--wx.App提供了基本的最简单的OnInit()方法  -- 适用于系统仅含一个窗口
# """
# import wx  # 导入wxPython模块
#
# app = wx.App()  # 创建wx应用程序对象
# frame = wx.Frame(parent=None, title="Hello wxPython")  # 创建一个顶级窗口
# frame.Show()  # 显示窗口
# app.MainLoop()  # 调用wx.App类的MainLoop()主循环方法 --Driver for wxPython App
#
# wx.Frame(parent=None, id=-1, title="", pos=wx.DefaultPosition, size=wx.DefaultSize,
#          style=wx.DEFAULT_FRAME_STYLE, name="frame")

# """
#     使用wx.Frame框架
# """
# import wx  # 导入wxPython module
#
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, id):  # 该__init__(params)出现在wx.Frame.__init__(params_list)中数目、顺序、表现形式完全一致--否则报错
#         wx.Frame.__init__(self, parent, id, title="创建Frame",
#                           pos=(100, 100), size=(686, 686))
#
#
# if __name__ == '__main__':
#     app = wx.App()  # 初始化应用
#     frame = MyFrame(parent=None, id=-1)  # 实例化MyFrame类，并传递参数
#     frame.Show()
#     app.MainLoop()

"""
    使用wx.StaticText输出Python之禅
"""
# import this
import wx  # import wxPython module


class MyFrame(wx.Frame):  # define subclass of wx.Frame
    def __init__(self, parent, id):  # rewrite __init__() method
        wx.Frame.__init__(self, parent, id, title="创建StaticText类", pos=(100, 100), size=(600, 400))
        panel = wx.Panel(self)  # 创建面板
        # 创建标题，并设置字体
        title = wx.StaticText(parent=panel, label="Python之禅——Tim Peters", pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font=font)
        # 创建文本
        wx.StaticText(panel, label="优美胜于丑陋", pos=(50, 50))
        wx.StaticText(panel, label="明了胜于晦涩", pos=(50, 70))
        wx.StaticText(panel, label="简洁胜于复杂", pos=(50, 90))
        wx.StaticText(panel, label="复杂胜于凌乱", pos=(50, 110))
        wx.StaticText(panel, label="扁平胜于嵌套", pos=(50, 130))
        wx.StaticText(panel, label="间隔胜于紧凑", pos=(50, 150))
        wx.StaticText(panel, label="可读性很重要", pos=(50, 170))
        wx.StaticText(panel, label="即便假借特例的实用性之名，也不可违背这些规则", pos=(50, 190))
        wx.StaticText(panel, label="不要包容所有错误，除非你确定要这样做", pos=(50, 210))
        wx.StaticText(panel, label="当存在多种可能，不要尝试去猜测", pos=(50, 230))
        wx.StaticText(panel, label="而是尽量找一种，最好是唯一一种明显的解决方案", pos=(50, 250))
        wx.StaticText(panel, label="虽然这并不容易，因为你不是 Python 之父", pos=(50, 270))
        wx.StaticText(panel, label="做也许好过不做，但不假思索就做还不如不做", pos=(50, 290))
        wx.StaticText(panel, label="如果你无法像人描述你的方案，那肯定不是一个好方案；反之亦然", pos=(50, 310))
        wx.StaticText(panel, label="命名空间十一给绝妙的理念，我们应当多加利用", pos=(50, 330))


if __name__ == '__main__':
    app = wx.App()  # 初始化应用
    frame = MyFrame(parent=None, id= -1)
    frame.Show()  # 显示窗口
    app.MainLoop()  # App对象app控制事件主循环--即程序动力(force)
