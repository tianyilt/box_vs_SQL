import pymysql

db = pymysql.connect('localhost', 'root', '123456', 'test', charset="utf8")
sur = db.cursor()

sur.execute('SET NAMES utf8;')
sur.execute('SET CHARACTER SET utf8;')
sur.execute('SET character_set_connection=utf8;')
sur.execute("drop table if exists Question")
sql_create = """create table Question (person char(200),question varchar(200))"""
sur.execute(sql_create)
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