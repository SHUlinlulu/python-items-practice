"""
    安装使用pymysql模块
"""
import pymysql

# 1. 获取 conn 对象
conn = pymysql.connect(
    host='127.0.0.1',  # <==> 'localhost'
    db='itheima',
    user='root',
    password='qq093135'
)

# 2. connection object's method "cursor()"-->获取 cursor 对象
cursor = conn.cursor()

# 3. create a empty table called "books"
sql = """
    create table books(
        book_id int(10) not null auto_increment,
        book_name varchar(100) not null,
        book_category varchar(100) not null,
        book_price decimal(10,2) default null,
        book_publish_time date default null,
        primary key (book_id)
    )auto_increment=1 default charset=utf8;
"""
cursor.execute("drop table if exists books")
cursor.execute(sql)

# 向books表格中executemany(iterator)插入批量数据--占位符看好了
book_list = [("零基础学Python", "Python", '79.80', '2018-5-20'),
             ("Python从入门到精通", "Python", '69.80', '2018-6-18'),
             ("PHP项目开发实战入门", 'PHP', '79.80', '2020-1-12'),
             ("Python小白入门", 'Python', '38.50', '2019-3-29'),
             ("零基础学Java", 'Java', '78.80', '2012-12-20'),
             ('大话设计模式(Java 版)', 'Java', '45.50', '2017-9-12')]
try:
    sql_sentence = "insert into books(book_name, book_category, book_price, book_publish_time) values(%s, %s, %s, %s)"
    cursor.executemany(sql_sentence, book_list)
    conn.commit()  # 提交数据
except:
    # 发生错误时回滚
    conn.rollback()

# close cursor
cursor.close()

# connection close
conn.close()
