
from xuexisql.MySQL import Mysql

host = 'localhost'
user = 'root'
password = 'zhoudunyi'
port = '3306'
database = 'sys'

mysql = Mysql(host, user, password, database)

sql = "select * from user ;"
result = mysql.get_one(sql)
if result:
    print(result)
