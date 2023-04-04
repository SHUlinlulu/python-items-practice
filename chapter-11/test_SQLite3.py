"""
    测试使用Python内置模块SQLite3
"""
import sqlite3

# 连接SQLite DB
# 数据库文件是sqlite.db, 若文件不存在，则在当前目录创建
conn = sqlite3.connect(database='sqlite.db')

# 创建一个cursor
cursor = conn.cursor()

# 执行一条sql语句
cursor.execute('create table user(id int(10) primary key, name varchar(20))')

# 关闭cursor
cursor.close()
# 关闭conn
conn.close()
