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
