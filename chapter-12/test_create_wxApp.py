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

# """
#     使用wx.StaticText输出Python之禅
# """
# # import this
# import wx  # import wxPython module
#
#
# class MyFrame(wx.Frame):  # define subclass of wx.Frame
#     def __init__(self, parent, id):  # rewrite __init__() method
#         wx.Frame.__init__(self, parent, id, title="创建StaticText类", pos=(100, 100), size=(600, 400))
#         panel = wx.Panel(self)  # 创建面板
#         # 创建标题，并设置字体
#         title = wx.StaticText(parent=panel, label="Python之禅——Tim Peters", pos=(100, 20))
#         font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
#         title.SetFont(font=font)
#         # 创建文本
#         wx.StaticText(panel, label="优美胜于丑陋", pos=(50, 50))
#         wx.StaticText(panel, label="明了胜于晦涩", pos=(50, 70))
#         wx.StaticText(panel, label="简洁胜于复杂", pos=(50, 90))
#         wx.StaticText(panel, label="复杂胜于凌乱", pos=(50, 110))
#         wx.StaticText(panel, label="扁平胜于嵌套", pos=(50, 130))
#         wx.StaticText(panel, label="间隔胜于紧凑", pos=(50, 150))
#         wx.StaticText(panel, label="可读性很重要", pos=(50, 170))
#         wx.StaticText(panel, label="即便假借特例的实用性之名，也不可违背这些规则", pos=(50, 190))
#         wx.StaticText(panel, label="不要包容所有错误，除非你确定要这样做", pos=(50, 210))
#         wx.StaticText(panel, label="当存在多种可能，不要尝试去猜测", pos=(50, 230))
#         wx.StaticText(panel, label="而是尽量找一种，最好是唯一一种明显的解决方案", pos=(50, 250))
#         wx.StaticText(panel, label="虽然这并不容易，因为你不是 Python 之父", pos=(50, 270))
#         wx.StaticText(panel, label="做也许好过不做，但不假思索就做还不如不做", pos=(50, 290))
#         wx.StaticText(panel, label="如果你无法像人描述你的方案，那肯定不是一个好方案；反之亦然", pos=(50, 310))
#         wx.StaticText(panel, label="命名空间十一给绝妙的理念，我们应当多加利用", pos=(50, 330))
#
#
# if __name__ == '__main__':
#     app = wx.App()  # 初始化应用
#     frame = MyFrame(parent=None, id=-1)
#     frame.Show()  # 显示窗口
#     app.MainLoop()  # App对象app控制事件主循环--即程序动力(force)

# """
#     使用wx.TextCtrl与wx.StaticText实现一个简易的用户登录界面
# """
# import wx  # import wxPython module
#
#
# class MyFrame(wx.Frame):  # define the subclass of wx.Frame
#     def __init__(self, parent, id):  # rewrite the __init__() method
#         wx.Frame.__init__(self, parent, id, title="Create a login interface of user",
#                           pos=(200, 100), size=(400, 300))
#         panel = wx.Panel(self)  # define a panel, panel is a window without boundary and title
#         # define text and input_box
#         self.title = wx.StaticText(panel, label="请输入用户名和密码", pos=(140, 20))
#         self.label_user = wx.StaticText(panel, label="用户名：", pos=(50, 50))
#         self.text_user = wx.TextCtrl(panel, value="", pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
#         self.label_pwd = wx.StaticText(panel, label="密 码：", pos=(50, 90))
#         self.text_pwd = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)
#         # define 'OK'  &  'Cancel' buttons
#         self.bt_confirm = wx.Button(panel, label="确定", pos=(105, 130))
#         self.bt_cancel = wx.Button(panel, label="取消", pos=(195, 130))
#
#
# if __name__ == '__main__':
#     app = wx.App()  # initial the application
#     frame = MyFrame(parent=None, id=-1)  # top frame
#     frame.Show()  # display the frame
#     app.MainLoop()  # drive the application running

"""
    使用事件判断用户登录  &&  BoxSizer布局
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="用户登录", size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="请输入用户名和密码")
        # 创建“确定“和”取消“按钮，并绑定事件
        self.bt_confirm = wx.Button(panel, label="确定")
        self.bt_confirm.Bind(event=wx.EVT_BUTTON, handler=self.OnClickSubmit)
        self.bt_cancel = wx.Button(panel, label="取消")
        self.bt_cancel.Bind(event=wx.EVT_BUTTON, handler=self.OnClickCancel)
        # 创建文本，左对齐
        self.label_user = wx.StaticText(panel, label="用户名：")
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label="密  码：")
        self.text_pwd = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 添加容器，容器中的控件横向排列
        # h_sizer_user
        h_sizer_user = wx.BoxSizer(orient=wx.HORIZONTAL)
        h_sizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        h_sizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        # h_sizer_pwd
        h_sizer_pwd = wx.BoxSizer(orient=wx.HORIZONTAL)
        h_sizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        h_sizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)
        # h_sizer_btn
        h_sizer_btn = wx.BoxSizer(orient=wx.HORIZONTAL)
        h_sizer_btn.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTRE, border=5)
        h_sizer_btn.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTRE, border=5)
        # 添加容器--，容器中的控件纵向排列
        v_sizer_all = wx.BoxSizer(orient=wx.VERTICAL)
        v_sizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTRE, border=15)
        v_sizer_all.Add(h_sizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        v_sizer_all.Add(h_sizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        v_sizer_all.Add(h_sizer_btn, proportion=0, flag=wx.ALIGN_CENTRE | wx.TOP, border=15)
        panel.SetSizer(v_sizer_all)

    def OnClickSubmit(self, event):  # 必须有这么个event参数占位
        """单击确定按钮，执行方法"""
        message = ""
        username = self.text_user.GetValue()  # 获取输入的用户名
        password = self.text_pwd.GetValue()  # 获取输入密码
        if username == "" or password == "":
            message = "用户名或密码不能为空"
        elif username == 'linlulu' and password == 'root':
            message = "登录成功"
        else:
            message = "输入的用户名与密码不匹配"
        wx.MessageBox(message=message)  # 弹出提示框

    def OnClickCancel(self, event):
        """单击取消按钮，执行该方法"""
        self.text_user.SetValue("")  # 清空输入的用户名
        self.text_pwd.SetValue("")  # 清空输入的密码


if __name__ == '__main__':
    app = wx.App()  # 初始化应用
    frame = MyFrame(parent=None, id=-1)
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法
