import pymysql
"""
这只是一个链接数据库的demo
"""
db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
sur = db.cursor()

sur.execute('SET NAMES utf8;')
sur.execute('SET CHARACTER SET utf8;')
sur.execute('SET character_set_connection=utf8;')
sur.execute("drop table if exists Question")
sql_create = """create table Question (person char(200),question varchar(200))"""
sur.execute(sql_create)

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
sur.execute(sql)

db.commit()
while nt:
    data = getData(soup)
    for item in data:
        sqlinsert = """insert into Question(person,question) values ('%s','%s')""" % (
        pymysql.escape_string(item[1]), pymysql.escape_string(item[0]))
        sur.execute(sqlinsert)

    soup = getSoup(url + nt, headers)
    nt = nextUrl(soup)
db.commit()
db.close()