"""
打印九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {j * i}\t", end=' ')
    print("")  # 莫忘了换行
