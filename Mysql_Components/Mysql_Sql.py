import pymysql


class Mysql_Sql(object):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = pymysql.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)

    def conn(self):     # 连接数据库
        try:
            self.db = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            return "连接成功"
        except pymysql.err.OperationalError as err:
            print(err.__str__())
            return "连接失败"

    def close(self):    # 关闭数据库
        self.db.close()

    def select(self, sql):  # 查询
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except:
            print("查询失败！")

        finally:
            self.db.close()
    
    def insert(self,sql):   #插入数据
        self.cursor = self.db.cursor()
        try:
            # self.cursor.execute(sql)
            tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            self.db.commit()
            return tt
        except:
            return "插入失败"
        finally:
            self.db.close()
    

    def update(self,sql):   #更新数据
        self.cursor = self.db.cursor()
        try:
            tt = self.cursor.execute(sql)  # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            self.db.commit()
            return tt
        except:
            return "更新失败"
        finally:
            self.db.close()

    def delele(self,sql):   #删除数据
        self.cursor = self.db.cursor()
        try:
            tt = self.cursor.execute(sql)  # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            self.db.commit()
            return tt
        except:
            return "删除失败"
        finally:
            self.db.close()