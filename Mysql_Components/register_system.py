import Mysql_Sql

def register_system(user, pw):
    mysqlconn = Mysql_Sql.Mysql_Sql(
        "localhost", "root", "zhjq2001", "student_system")
    sql="INSERT INTO `user` ( username, password,type ) VALUES ('%s', '%s','%s'); "%(user,pw,"学生")
    flag=mysqlconn.insert(sql)
    return flag
