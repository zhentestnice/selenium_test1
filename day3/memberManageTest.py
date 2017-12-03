import unittest

import time
from selenium import webdriver


class MemberManageTest(unittest.TestCase):
    #变量前面加上self.表示这个变量是类的属性,可以被其他方法访问
    def setUp(self):
        #driver声明在setUp方法之内,不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        #quit()是退出整个浏览器
        #close()关闭浏览器其中一个标签
        time.sleep(20)#工作中正式运行不需要,代码编写和调试时需要加等待
        self.driver.quit()

    def test_add_mamber(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("随意22")
        driver.find_element_by_name("mobile_phone").send_keys("13454851456")
        driver.find_element_by_css_selector('[value="1"]')
        driver.find_element_by_id("birthday").send_keys("2017-11-11")
        driver.find_element_by_name("email").send_keys("1048526451@qq.com")
        driver.find_element_by_name("qq").send_keys("1048526451")
        #driver.find_element_by_class_name("button_search").click()