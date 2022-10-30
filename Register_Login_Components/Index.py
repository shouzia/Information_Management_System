import First_Page
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')
from Mysql_Components.login_system import login

login_register_flag = First_Page.login_register()

if login_register_flag == "登录":
    login("admin", "admin")
else:
    print("注册")
