#1.打开浏览器
from selenium import webdriver
#从 selenium 导入 网络驱动,用来操作浏览器
driver = webdriver.Chrome()
#2.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3.输入账号,首先寻找用户名的输入框
#网页上所有可见的都属于element,比如link,按钮,下拉框
driver.find_element_by_id("username").send_keys("zhen_test")
#4.输入密码
driver.find_element_by_id("password").send_keys("1234qwer")
#5.点击登录按钮
#如果我使用一个方法,这个方法没有提示信息,这个方法是不存在的
driver.find_element_by_class_name("login_btn").click()