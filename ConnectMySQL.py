import pymysql
"""
这只是一个链接数据库的demo
"""
db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")

cursor = db.cursor()

#SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

db.close()