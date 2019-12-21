import pymysql

# 打开数据库连接
db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * from dashboard;"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()#return tuple
    for row in results:
        UID = row[0]
        MaxScore = row[1]
        # 打印结果
        print("UID=%s,MaxScore=%s" % \
              (UID, MaxScore))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()