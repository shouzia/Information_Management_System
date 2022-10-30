import First_Page

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')
from Mysql_Components.login_system import login
from Mysql_Components.register_system import register_system
from Login import Login 



login_register_flag = First_Page.login_register()

if login_register_flag == "登录":
    user=input("输入用户名:")
    passwrod=input("输入密码:")
    Login=Login(user,passwrod,login(user, passwrod))
    Login.usertype_judge()
else:
    user=input("输入用户名:")
    passwrod=input("输入密码:")
    flag=register_system(user,passwrod)
    if flag!=1:
        print("注册失败")
    else:
        print("注册成功")
