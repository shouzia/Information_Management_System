import Mysql_Sql

sql = Mysql_Sql.Mysql_Sql("localhost", "root", "zhjq2001", "student_system")
print(sql.conn())
data = sql.select("SELECT * FROM user")
for row in data:
    userid = row[0]
    name = row[1]
    sex = row[2]
    if userid == "admin":
        print(sex)
    # 打印结果
    print("学号=%s,姓名=%s,性别=%s" %
          (userid, name, sex,))
