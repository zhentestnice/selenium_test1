#javascript是一门独立的语言
#要想学习好selenium最重要的三件事
# 1.元素定位优先级:ID>name>class>link_text(link必须是链接,<a>标签,必须是文本)
#2.元素的操作:鼠标左键单击click,发送键盘按键send_keys
#3.javascript学好
#用javascript实现窗口切换
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")

js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)

driver.find_element_by_link_text("登录").click()

driver.find_element_by_id("username").send_keys("zhen_test")