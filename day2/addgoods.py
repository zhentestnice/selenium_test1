from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
#1.登录
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
#2.商品管理
driver.find_element_by_link_text("商品管理").click()
#3.添加商品
driver.find_element_by_link_text("添加商品").click()
#4.商品名称
#有一种特殊的网页,比如左边或上面有导航条
#其中"商品管理"和"添加商品"属于页面根节点的网页
#商品名称属于frame框架中的子网页
#现在需要切换网页
driver.switch_to.frame("mainFrame")   #切换到子框架
driver.find_element_by_name("name").send_keys("iphone 7")
#5.商品分类
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
#driver.find_element_by_id("7").click()
#双击是一种特殊的元素操作,被封装到ActionChains这个类里,java封装到Actions这个类里
#链表必须以perform()结束
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()

#driver.find_element_by_link_text("选择当前分类").click()
#6.商品品牌

pinpai = driver.find_element_by_tag_name("select")
Select(pinpai).select_by_visible_text("苹果 (Apple)")

#7.提交
#driver.find_element_by_class_name("button_search").click()