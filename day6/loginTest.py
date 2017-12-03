import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #1.打开网页
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp = LoginPage(self.driver)
        lp.open()
        #2.输入用户名
        lp.input_username("zhen_test")
        #self.driver.find_element(By.ID,"username").send_keys("zhen_test")
        #3.输入密码
        lp.input_password("1234qwer")
        #self.driver.find_element(By.ID,"password").send_keys("1234qwer")
        #4.点击登录页面
        lp.click_login_button()
        #self.driver.find_element(By.CLASS_NAME,"login_btn").click()
        #5.验证是否跳转到管理中心页面
        pcp = PersonalCenterPage(self.driver)
        #expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        time.sleep(5)
        self.assertIn(pcp.title,self.driver.title)