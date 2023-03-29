"""
    测试使用Python中的文件相关操作
"""
# file = open("F://temp_code_files/test.txt", 'r', encoding="utf-8")
# contents = file.readlines()
# for line in contents:
#     print(line)

with open("F://temp_code_files/demo.txt", 'w', encoding='utf-8') as file:
    str_list = ["itheima是一家线上IT教学平台", "https://www.itcast.com是itheima公司的官方网址", "Caoyu is member of this company"]
    file.writelines(str_list)
    file.flush()  # 不使用flush,文件根本就没有真正写入，也就读不出内容

    # file_list = file.readlines()
    new_file = open("F://temp_code_files/demo.txt", 'r', encoding="utf-8")
    file_str = new_file.readlines()
    print(f"file_str = {file_str}")
    # print(f"file_list = {file_list}")
