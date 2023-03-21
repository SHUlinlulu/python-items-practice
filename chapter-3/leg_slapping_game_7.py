"""
逢七拍腿游戏
描述：1~99数数，遇到以7结尾或7的倍数，拍一下腿，问共拍腿次数？
learned：
    1.体会到str内置方法的多样性
    2.逆向思维的应用
"""
count = 99  # 最大拍腿次数
for i in range(1, 100):
    if i % 7 == 0:
        continue
    elif str(i).endswith('7'):  # endswith(ch)->bool 判断字符串是否以ch结尾
        continue
    else:  # 有无else不影响程序的逻辑正确性--->continue略过了后续语句
        count -= 1

print("1~99共拍腿次数:", count, "次")
