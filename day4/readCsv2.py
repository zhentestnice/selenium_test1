#1.之前的csv不能被其他测试用例调用,所以应该给这段代码封装到一个方法里
#2.每个测试用例的路径不同,所以path应该作为参数传入到这个方法中
#3.我们打开了一个文件但是没有关闭,最终可能导致内存泄露
import csv
import os


def read(file_name):
    #所有的重复代码的出现,都是程序设计不合理
    #重复的代码都应该封装到一个方法里
    basepath = os.path.dirname(__file__)
    path = basepath.replace("day4", "data/" + file_name)  # csv文件的路径
    #file = open(path,'r')
    #with语句可以自动关闭with中声明的变量file
    #try...finally...也可以实现,但是可读性比较差,写起来容易出错,一般用with语句代替
    #因为文件一旦关闭,里面的数据也会消失,所以单独声明一个列表,来保存里面的数据
    result = []
    with open(path,'r') as file:
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
    return result
    #如果再打开后的代码中出现异常,后面的代码不能正常运行,file.close()不执行
    #应该用with...as...语句实现实现
    #file.close()

if __name__ == '__main__':
    #path1 = r"C:\Users\51Testing\PycharmProjects\selenium_test1\data\member_info.csv"
    #这个路径是绝对路径,我们工作中一个项目不止一个人编写代码,我们没法统一要求大家都把项目代码放在一个路径下
    #所以应该在代码中,通过当前代码文件的路径,根据相对位置找到csv文件相对路径
    #首先找到当前文件的路径
    #__file__是python内置变量,指的是当前文件
    member_info = read("member_info.csv")
    for row in member_info:
        int(row[2])

    #print(member_info)
#5.读出数据不是目的,目的是使用里面的数据驱动测试,应该把数据作为方法的返回值方便进一步调用