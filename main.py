import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='zhjq2001',
                     database='sutdent')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用 execute()  方法执行 SQL 查询
sql = "SELECT * FROM userdata"

# # 使用 fetchone() 方法获取单条数据.
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        userid = row[0]
        name = row[1]
        sex = row[2]
        income = row[3]
        xueyuan = row[4]
        # 打印结果
        print("学号=%s,姓名=%s,性别=%s,籍贯=%s,学院n=%s" %
              (userid, name, sex, income, xueyuan))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
