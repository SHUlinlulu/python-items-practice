"""
    测试使用Python中的fetchone(),fetchmany(size),fetchall()方法获取结果集result中的数据
"""
# import corresponding modules
import pymysql

# 1. obtain connection object
conn = pymysql.connect(
    host="localhost",
    db="itheima",
    user="root",
    passwd="qq093135"
)

# 2. obtain cursor object through connection object's method called "cursor()"
cursor = conn.cursor()
# 3. statement sql phrase
"""
    注意：--均使用%s作为占位符，否则会报错----一些莫名的错误，看都看不懂
"""
sql_1 = '''insert into books(book_name, book_category, book_price, book_publish_time)
        values(%s, %s, %s, %s);'''  # 增
sql_2 = '''delete from books where book_name = %s;'''  # 删
sql_3 = '''update books set book_price = %s where book_id = %s;'''  # 改
sql_4 = '''select * from books where book_category = %s;'''  # 查

# execute sql sentence to operate database
# cursor.execute(sql_1, ('Java编程思想', 'Java', 79.90, '2018-3-15'))
# cursor.execute(sql_2, ('Python从入门到精通',))
# cursor.execute(sql_3, ('52.50', 4))
cursor.execute(sql_4, ('Java',))
result_1 = cursor.fetchone()
# result_2 = cursor.fetchmany(2)
result_3 = cursor.fetchall()
conn.commit()
print(f"result_1 = {result_1}")
# print(f"result_2 = {result_2}")
print(f"result_3 = {result_3}")

# close cursor
cursor.close()
# close conn
conn.close()



