class Login():
    def __init__(self,user,password,usertype):
        self.user=user
        self.password=password
        self.usertype=usertype
    
    def usertype_judge(self):
        if self.usertype=="管理员":
            print("管理员")
        elif self.usertype=="老师":
            print("老师")
        elif self.usertype=="学生":
            print("学生")


    def login_admin(self):
        print("管理员")
