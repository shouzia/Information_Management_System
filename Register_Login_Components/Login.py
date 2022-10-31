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
            print("老师" )
        elif self.usertype=="学生":
            print("学生")


    def login_admin(self,flag):
        if flag==0:
            print("修改")
        elif flag==1:
            print("注册")
        else:
            print("输入错误")

