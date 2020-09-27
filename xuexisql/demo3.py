
from xuexisql.MySQL  import Mysql
import  pymysql

host = 'localhost'
user = 'root'
password = 'zhoudunyi'
port = '3306'
database = 'sys'
cursorclass = pymysql.cursors.DictCursor

if __name__ == '__main__':
    mysql = Mysql(host,user,password,database)
    # sql ="create table user(id INT auto_increment primar key,name varchar(30),age int )"

    '''
    测试创建表
    '''
    '''
    res = mysql.updata(sql)
    if res:
        sql2="select * from user ;"
        mysql.get_one(sql2)
        print(res)
    else:
        print("数据库创建失败！")
    '''

    sql ='insert into user value (null,"zhangsan",18)'
    res = mysql.insert(sql)
    if res:
        sql2 = "select * frome user；"
        re = mysql.get_one(sql2)
        print(re)
    else:
        print("数据库插入失败！")
