from config import ConnetMysql

def register_system(user, pw,usertype="学生"):
    mysqlconn = ConnetMysql()
    sql="INSERT INTO `user` ( username, password,type ) VALUES ('%s', '%s','%s'); "%(user,pw,usertype)
    flag=mysqlconn.insert(sql)
    return flag

