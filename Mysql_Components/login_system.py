
import Mysql_Sql


# 登陆系统


def login(user, password):

    mysqlconn = Mysql_Sql.Mysql_Sql(
        "localhost", "root", "zhjq2001", "student_system")
    print(mysqlconn.conn())
    sql = "SELECT * FROM `user` WHERE username='" + \
        user + "' AND password='"+password+"'"
    data = mysqlconn.select(sql)
    for row in data:
        username = row[0]
        password = row[1]
        type = row[2]
        if username == user and password == password:
            print(type)
            return type