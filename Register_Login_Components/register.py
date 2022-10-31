import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')
from Mysql_Components.select_user import select_user

class Register():
    def __init__(self,user,password,password2,usertype):
        self.user=user
        self.password=password
        self.password2=password2
        self.usertype=usertype


    def confirm_username(self): #确认用户名是否存在
        user=self.user
        data=select_user(user)
        flag=False
        if data == ():
            # 用户名不存在可以注册
            flag=True
            return flag
        else:
            print("用户名存在")
            flag=False
            return flag


    def confirm_password(self):     #确认密码
        password=self.password
        password2=self.password2
        if password==password2:
            return True
        else:
            print("请确认二次密码是否一致")
            return False
    

    def confirm_register(self):
        flag_user=Register(self.user,self.password,self.password2,self.usertype).confirm_username()
        flag_password=Register(self.user,self.password,self.password2,self.usertype).confirm_password()
        if flag_user and flag_password:
            return True
        else:
            return False

