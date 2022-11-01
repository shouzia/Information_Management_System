import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')

from Mysql_Components.register_system import register_system


def register_advanced():
    username=input("输入用户名:")
    passworrd=input("输入密码:")
    usertype=input("输入用户类型:")
    flag=register_system(username,passworrd,usertype)
    return flag
