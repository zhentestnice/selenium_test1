#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#2.点击登录连接
driver.find_element_by_link_text("登录").click()
cwh = driver.current_window_handle
whs = driver.window_handles
for item in whs:
    if item != whs:
        driver.switch_to.window(item)
    else:
        driver.close()
#3.输入用户名密码
driver.find_element_by_id("username").send_keys("zhen_test")
driver.find_element_by_id("password").send_keys("1234qwer")
#4.点击登录按钮