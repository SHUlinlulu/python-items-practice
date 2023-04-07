"""
    测试使用GUI界面设计模块wxPython
"""
import wx


class App(wx.App):  # 创建一个wx.App的子类App
    # 初始化方法
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wxPython')  # 创建窗口
        frame.Show()  # 显示窗口
        return True


if __name__ == '__main__':
    app = App()  # 创建App类的实例对象
    app.MainLoop()  # 调用App类的MainLoop()主循环方法
