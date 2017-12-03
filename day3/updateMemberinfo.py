#1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("zhen_test")
#driver.find_element_by_id("username").send_keys(Keys.TAB)
#l链表必须有明确的结束标志
ActionChains(driver).send_keys(Keys.TAB).send_keys("1234qwer").send_keys(Keys.ENTER).perform()    #点击tab键切换
#2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
#3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
#4.修改个人信息
#更好的编程习惯是,在每次sendkeys之前都进行clear操作
driver.find_element_by_id("true_name").clear()    #清空输入框
driver.find_element_by_id("true_name").send_keys("随便")
#css可以用多个属性定位一个元素,多个属性之间不能有空格('#xbvalue="2"')
driver.find_element_by_css_selector('[value="2"]').click()
#修改日期
#js = 'document.getElementById("date").removeAttribute("readonly")'
#driver.execute_script(js)
#driver.find_element_by_id("date").clear()
#driver.find_element_by_id("date").send_keys("2017-11-11")
#用arguments写上面的功能,用selenium的定位方式定位元素更简单,
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("2017-11-11")

#用selenium调用javascript一共有两个关键字:
# 1.arguments[0]:表示用python语言代替一部分javascript,好处是有时selenium定位比较容易
# 2.return 把javascript的执行结果返回给python语言,好处是有时selenium定位不到的元素,可以用javascript定位到
#date = driver.execute_script("return document.getElementById('date')")
#这句话等于clac = driver.find_element_by_id("date")

driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1048965814")
driver.find_element_by_class_name("btn4").click()
#这种右键检查不了的html代码的弹出框叫alert,有单独的方法处理
time.sleep(3)
#alert控件不是html生成的,所以implicitly_wait对这个控件不管用
#所以time.sleep()方法不能省略,要和implicitly_wait组合使用
#切换到alert的方法和切换窗口的方法类似
#alert:弹出框,accept:接受,确认,dismiss:拒绝,取消
driver.switch_to.alert.accept()
