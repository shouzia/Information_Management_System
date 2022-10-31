from config import ConnetMysql

def register_system(user, pw):
    mysqlconn = ConnetMysql()
    sql="INSERT INTO `user` ( username, password,type ) VALUES ('%s', '%s','%s'); "%(user,pw,"学生")
    flag=mysqlconn.insert(sql)
    return flag
