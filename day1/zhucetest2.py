#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
#2.打开网站首页
driver.get("http://localhost/")
#3.点击注册连接
#第四种元素定位方法:链接的文本信息
driver.find_element_by_link_text("注册").click()
#driver.find_element_by_name("keyword").send_keys("zhentest")
#窗口切换:把selenium切换到新的窗口工作
cwh = driver.current_window_handle    #浏览器当前窗口的句柄
#selenium只提供了工作窗口的名字,并没有提供第二个窗口的名字,需自己求
whs = driver.window_handles   #浏览器中所有窗口的句柄
for item in whs:
    if item == whs:
        driver.close()  #关闭当前标签
    else:
        driver.switch_to.window(item)    #此方法将下划线换成点

#4.输入用户名
driver.find_element_by_name("username").send_keys("zhentest")
#5.点击提交