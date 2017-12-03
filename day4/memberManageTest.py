import unittest
import ddt  #导入代码库
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

#2.装饰这个类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #3.调用之前写好的read()方法,获取配置文件中的数据
    member_info = read("member_info.csv")

    #在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前,只执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()

    #python中集合前面的 星号表示把集合中的元素拆开,一个一个写
    #list=["a","b"]
    #*list= "a","b",一个列表,变成两个字符串
    #假如一个方法需要接收两个元素,那么肯定不能传一个list进去
    #但是如果list中正好也是两个元素,这时在列表前面加一个星号,这时就不是一个列表,是两个参数了
    #@ddt.data()测试数据来源于read()方法
    #5.把数据表中的每一行传入方法,在方法中增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        #print("添加会员")
        driver = self.driver
        #每组测试数据就是一条测试用例,每条测试用例应该是独立的,不能因为一条测试用例执行失败,导致下一条用例不能正常执行,所以不推荐用for循环
        #应该用ddt装饰器,去修饰这个方法,达到每条测试用例独立执行的目的
        #ddt是数据驱动测试,data driver test

        #4.注释掉for循环
        #for row in read("member_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        #driver.switch_to.frame("mainFrame")
        #当iframe没有name属性时,可以通过其他方式定位元素
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value="'+row[2]+'"]').click()
        #driver.find_element_by_css_selector('[value="{0}"].format(row[2])').click()
        #format()格式化输出
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        #actual:实际结果,执行测试用例后页面上实际显示的结果
        #expected:期望结果,来自于手动测试用或者需求文档或配置文件
        time.sleep(3)
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        expected = row[0]
        #断言类似于if...else...,是用来做判断的
        # if expected == actual:
        #     print("pass")
        # else:
        #     print("fail")
        #断言是assert,断言是框架提供的,要想调用断言,必须加self.因为测试用例类继承了框架中的TestCase类,也继承了这个类的断言,所以可以直接用断言的方法
        #断言有几个特点:
        #1.断言比较简洁
        #2.断言只关注错误的测试用例,只有断言出错的时候才会打印信息
        #3.断言报错时,后面的代码不会继续执行,前面的步骤失败,后面的步骤就不需要继续尝试了


        #切换到父框架
        driver.switch_to.parent_frame()
        self.assertEqual(expected, actual)
        #切换到网页的根节点
        #driver.switch_to.default_content()

if __name__ == '__main__':
    unittest.main()