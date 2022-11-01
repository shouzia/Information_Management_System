import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../admin',)
sys.path.append('../teacher',)

from admin.change_user import change_user
from admin.register_advanced import register_advanced

from teacher.Select_Change_studentdata import Select_Change_studentdata


class Login():
    def __init__(self,user,password,usertype):
        self.user=user
        self.password=password
        self.usertype=usertype
    
    def usertype_judge(self):
        if self.usertype=="管理员":
            print("----------管理员----------")
            print("0-----修改用户信息")
            print("1-----注册----教师")
            option = int(input("请选择:"))
            Login(self.user,self.password,self.usertype).login_admin(option)
        elif self.usertype=="老师":
            print("----------老师----------")
            print("0-----修改学生信息")
            print("1-----修改学生成绩")
            option=int(input("请选择"))
            Login(self.user,self.password,self.usertype).login_teacher(option)
        elif self.usertype=="学生":
            print("学生")


    def login_admin(self,flag):
        if flag==0:
            data=change_user()
            if data==1:
                print("修改成功")
            else:
                print("修改失败")
        elif flag==1:
            data=register_advanced()
            if data==1:
                print("注册成功")
            else:
                print("注册失败")
        else:
            print("输入错误")
        

    def login_teacher(self,flag):
        if flag==0:
            data=Select_Change_studentdata().change_studentdata()
            if data==1:
                print("修改成功")
            else:
                print("修改失败")
        elif flag==1:
            data=Select_Change_studentdata().change_score()
            if data==1:
                print("修改成功")
            else:
                print("修改失败")
        else:
            print("输入错误")

