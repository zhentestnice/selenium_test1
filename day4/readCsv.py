#准备好一个csv文件
#1.导入csv包,csv是python内置的包,说明比selenium常用
import csv
#2.要想读取文件的信息,首先要知道文件存放路径
#字符串前面加r字符,表示后面字符串中反斜杠不是转义字符
path = r"C:\Users\51Testing\PycharmProjects\selenium_test1\data\member_info.csv"
#3.通过路径打开文件
file = open(path,'r')  #r表示只读
#4.通过csv代码库读取csv文件内容
data_table = csv.reader(file)
#5.遍历data_table,分别打印每一行数据
for row in data_table:
    print(row)