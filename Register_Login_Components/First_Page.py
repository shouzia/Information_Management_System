

def first_page() -> str:
    print("--------学生管理系统--------")
    print("0---登录")
    print("1---注册")

    flag = int(input("输入对应数字选择登录或注册"))
    return flag


def login_register():
    login_Flag = 0
    login_Flag = first_page()
    flag = ""
    i = 0
    while (i == 0):
        if login_Flag == 0:
            flag = "登录"
            print("登录")
            break
        elif login_Flag == 1:
            print("注册")
            flag = "注册"
            break
        else:
            login_register()
            break
    return flag
