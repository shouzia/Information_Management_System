import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')
from Mysql_Components.select_user import select_all 
from Mysql_Components.config  import ConnetMysql


class Select_Change_studentdata(object):
    def __init__(self,username=""):
        self.username=username

    def select_studentdata(self):
        data=select_all("student_data")
        for row in data :
            username=row[0]
            name=row[1]
            sex=row[2]
            phonenumber=row[3]
            addres=row[4]
            print("用户名:{} 姓名:{} 性别:{} 手机号:{} 地址:{}".format(username,name,sex,phonenumber,addres))
    def select_score(self):
        data=select_all("score")
        for row in data :
            username=row[0]
            name=row[1]
            chinese=row[2]
            math=row[3]
            english=row[4]
            print("用户名:{} 姓名:{} 语文成绩:{} 数学成绩:{} 英语成绩:{}".format(username,name,chinese,math,english))
    
    def change_studentdata(self):
        print("修改学生信息")
        Select_Change_studentdata().select_studentdata()
        self.username=input("输入学生用户名:")
        name=input("请输入新的学生姓名")
        sex=input("请输入新的性别")
        phonenumber=input("请输入新的手机号")
        address=input("请输入新的地址")
        conn=ConnetMysql()
        sql="UPDATE student_data SET name='"+name+"' ,sex='"+sex+"',phonenumber='"+phonenumber+"',address='"+address+"' WHERE username='"+self.username+"'"
        data=conn.update(sql)
        return data

    def change_score(self):
        print("修改学生成绩")
        Select_Change_studentdata().select_score()
        self.username=input("输入学生用户名:")
        chinese=int(input("请输入新的语文成绩"))
        math=int(input("请输入新的数学成绩"))
        english=int(input("请输入新的英语成绩"))
        conn=ConnetMysql()
        sql="UPDATE score SET chinese=%s ,math=%s,english=%s WHERE username='%s'"%(chinese,math,english,self.username)
        data=conn.update(sql)
        return data

