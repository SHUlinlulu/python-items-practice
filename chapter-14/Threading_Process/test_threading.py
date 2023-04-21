"""
    测试使用python提供的支持多线程的threading module下的Thread
"""
from threading import Thread  # 线程类
# '''
#     方式1实现多线程
# '''
# # 定义子线程方法
#
#
# def func():
#     for i in range(1000):
#         print("子线程", i)
#
#
# if __name__ == '__main__':  # 默认每个执行的程序都会自动创建一个主线程
#     thread = Thread(target=func)  # 创建子线程 thread
#     thread.start()  # 设置子线程func的执行状态为start,如此线程thread就可以根据cpu的调度进行执行了
#     # 执行的方法是Thread对象thread的run方法
#     for j in range(1000):
#         print("主线程", j)

'''
    方式2 -- 通过继承Thread类,改写其中的run方法,实现具体的子线程实现
    # 专业或者多数程序员更喜欢这种方式
'''


class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print("sub thread", i)


if __name__ == '__main__':
    my_thread = MyThread()  # 创建子线程对象
    my_thread.start()  # 设置子线程对象可以执行, 即： status --> start

    for j in range(1000):
        print("main thread", j)


