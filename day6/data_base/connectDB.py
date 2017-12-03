#1.导入pymysql代码库
import pymysql

def connectDb():
    #要想连接数据库,需要知道数据库:IP地址,端口号,用户名,密码,数据库名称
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root",database="pirate", port=3306, charset='utf8')
    #查询hd_user表中所有的数据,且倒序打印
    sql = "select * from hd_user order by id desc"
    #要想在代码中执行这条sql语句,首先要获取数据库的游标cursor
    curs = conn.cursor()
    #通过游标执行sql语句
    curs.execute(sql)
    #想要获取数据库中最新的记录,就要把数据库所有记录倒叙排列,然后用fetchone()方法获取第一条记录
    #获取所有用fetchall()
    result = curs.fetchone()
    return result
if __name__ == '__main__':
    #connectDb()
    print(connectDb())
