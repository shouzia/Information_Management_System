import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')

from Mysql_Components.config import ConnetMysql
from Mysql_Components.select_user import select_all


def change_user():
    user_data=select_all("user")
    for row in user_data:
        username=row[0]
        password=row[1]
        usertype=row[2]
        print("用户名:{} 密码:{} 用户类型:{}".format(username,password,usertype))
    user=input("输入需要修改的用户名")
    user_change=input("输入新的用户名")
    password_change=input("输入新的用户密码")
    usertype_change=input("输入新的用户类型")
    conn=ConnetMysql()
    sql="UPDATE user SET username='"+user_change+"' ,`password`='"+password_change+"',type='"+usertype_change+"' WHERE username='"+user+"'"
    data=conn.update(sql)
    return data
