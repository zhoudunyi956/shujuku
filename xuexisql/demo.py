#导包
import pymysql
#创建连接
host = 'localhost'
user = 'root'
password = 'zhoudunyi'
port = '3306'
database = 'mysql'

db = pymysql.connect(host,user,password,database)

#游标对象
cursor = db.cursor()

#编写sql语句并执行

sql = 'select * from mysql.db '
cursor.execute(sql)

#输出结果
# print(cursor.fetchone())#单条输出
print(cursor.fetchall())#全部输出


#关闭连接

cursor.close()
db.close()
