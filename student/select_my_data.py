import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))) # 当前项目路径加入
sys.path.append('../Mysql_Components')
from Mysql_Components.select_user import select_table_user

def select_my_data(user):
    data=select_table_user("student_data",user)
    for row in data:
        username=row[0]
        name=row[1]
        sex=row[2]
        phonenumber=row[3]
        addres=row[4]
        print("用户名:{} 姓名:{} 性别:{} 手机号:{} 地址:{}".format(username,name,sex,phonenumber,addres))


def select_my_score(user):
    data=select_table_user("score",user)
    for row in data:
        username=row[0]
        name=row[1]
        chinese=row[2]
        math=row[3]
        english=row[4]
        print("用户名:{} 姓名:{} 语文成绩:{} 数学成绩:{} 英语成绩:{}".format(username,name,chinese,math,english))

