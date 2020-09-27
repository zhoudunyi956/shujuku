import pymysql


class Mysql():
    # 传参数
    def __init__(self, host, user, password, database, cursorlclass=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        if cursorlclass:
            self.cursorclass = cursorlclass
        else:
            self.cursorlclass = None

    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, self.cursorlclass)
        self.cursor = self.db.cursor()

    def get_one(self, sql):
        result = 0
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except Exception as E:
            print("select error:", E)
        return result

    def get_all(self, sql):
        result = 0
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close
        except Exception as E:
            print("select error:", E)
            return result

    # 插入函数
    def insert(self, sql):
        return self._edit(sql)

    # 删除函数
    def delete(self, sql):
        return self._edit(sql)

    # 修改函数
    def updata(self, sql):
        return self._edit(sql)

    # 主函数：实现具体的功能
    def _edit(self, sql):
        result = 1
        try:
            self.connect()
            result = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as E:
            print('error:', E)
            result = 0
            self.db.rollback()
        return result

    def close(self):
        self.cursor.close()
        self.db.close()
