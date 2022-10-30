import Mysql_Sql

sql = Mysql_Sql.Mysql_Sql("localhost", "root", "zhjq2001", "sutdent")
print(sql.conn())
data = sql.select("SELECT * FROM userdata")
for row in data:
    userid = row[0]
    name = row[1]
    sex = row[2]
    income = row[3]
    xueyuan = row[4]
    # 打印结果
    print("学号=%s,姓名=%s,性别=%s,籍贯=%s,学院n=%s" %
          (userid, name, sex, income, xueyuan))
