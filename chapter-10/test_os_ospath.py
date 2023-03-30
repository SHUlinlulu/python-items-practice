# """
#     测试使用Python内置的os与os.path模块中的对于文件或目录的相关操作方法
# """
# import os
# if __name__ == '__main__':
#     print(os.name)
#     if os.name == 'nt':
#         print("当前操作系统是Windows")
#     else:
#         print("当前操作系统是Linux")
#     # 判断指定目录F://temp_code_files是否存在
#     if os.path.isdir(r"F:\temp_code_files"):
#         print(R"F:\temp_code_files 存在")
#     else:
#         print("Error: 指定目录不存在[^_^]")
#
"""
    调用os模块的stat()函数获取文件的基本信息并格式化输出
"""
# import os
# fileinfo = os.stat("F://temp_code_files/temp.png")
# print("索引号：", fileinfo.st_ino)
# print("设备名：", fileinfo.st_dev)
# print("文件大小：", fileinfo.st_size)  # B
# print("最后一次访问时间：", fileinfo.st_atime)
# print("最后一次修改时间：", fileinfo.st_mtime)
# print("最后一次状态变化时间：", fileinfo.st_ctime)


"""
    改进，为了使得显示更加直观，需要对这样的数据进行格式化
"""
# import os


def formattime(longtime):
    """
    格式化日期时间的函数
    :param longtime: 需要格式化的时间--float
    :return: 按照指定格式格式化好的日期时间字符串
    """
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(longtime))


def formatByte(number):
    """
    格式化文件的大小的函数
    :param number: 要格式化的字节数
    :return: 格式化好的文件大小
    """
    for (scale, label) in [(1024 * 1024 * 1024, 'GB'), (1024 * 1024, 'MB'), (1024, 'KB')]:
        if number >= scale:  # 文件大小大于等于1KB
            return "%.2f %s" % (number * 1.0 / scale, label)
        elif number == 1:  # 文件大小为1B
            return "1 B"
        else:  # 处理小于1KB的情形
            pass
    return f"{number} B"


if __name__ == '__main__':

    import os
    fileinfo = os.stat("F://temp_code_files/temp.png")
    print("索引号：", fileinfo.st_ino)
    print("设备名：", fileinfo.st_dev)
    print("文件大小：", formatByte(fileinfo.st_size))  # B
    print("最后一次访问时间：", formattime(fileinfo.st_atime))
    print("最后一次修改时间：", formattime(fileinfo.st_mtime))
    print("最后一次状态变化时间：", formattime(fileinfo.st_ctime))
