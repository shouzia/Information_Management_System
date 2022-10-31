import Mysql_Sql

def ConnetMysql():
    conn=Mysql_Sql.Mysql_Sql("localhost", "root", "zhjq2001", "student_system")
    return conn
