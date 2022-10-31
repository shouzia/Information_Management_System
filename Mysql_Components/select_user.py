from config import ConnetMysql

def select_user(user):  #查询注册时用户名是否存在
    mysqlconn = ConnetMysql()
    sql = "SELECT * FROM `user` WHERE username='" + user +"'"
    data = mysqlconn.select(sql)
    return data 