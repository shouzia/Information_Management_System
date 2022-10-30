import Mysql_Sql


# 登陆系统
def login(user, pw):

    mysqlconn = Mysql_Sql.Mysql_Sql(
        "localhost", "root", "zhjq2001", "student_system")
    sql = "SELECT * FROM `user` WHERE username='" + \
        user + "' AND password='"+pw+"'"
    data = mysqlconn.select(sql)
    if data == ():
        print("登陆失败,请检查用户名或密码")
        return "登陆失败,请检查用户名或密码"
    else:
        for row in data:
            username=row[0]
            password=row[1]
            usertype=row[2]
        if username==user and password==pw:
            return usertype
