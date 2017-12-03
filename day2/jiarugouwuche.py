import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#隐式等待,一经设置,对后面所有语句都可以产生效果,所以在创建浏览器时设置一次就可以了
driver.implicitly_wait(30)   #implicitly:含蓄委婉
driver.maximize_window()  #窗口最大化
driver.get("http://localhost/")

#在点击登录按钮之前,先删除target属性
#用arguments关键字,把元素定位作为参数替换到javascript语句中
login_link = driver.find_element_by_link_text("登录")   #点击登录按钮
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()

driver.find_element_by_id("username").send_keys("zhen_test")
driver.find_element_by_id("password").send_keys("1234qwer")
driver.find_element_by_id("password").submit()
#submit()用于提交form表单,form是html中的一个元素
#form表单中任何子孙节点都可以调用submit()方法提交表单

#time.sleep(5)  #alt+enter 选择导入包
#time.sleep设置几秒都不好,应该使用隐式等待,自动判断网页是否加载完毕,完毕后再开始查找且需要设置最大时间,不能让程序无限等待,一般为30s
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#iphone_img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
iphone_link = "div.shop_01-imgbox > a"
#img是标签名,>标签前面的是父节点,后面是子节点
#如果想在css中写class属性,那么前面需要加上小数点
#:nth-child(2),表示是当前节点的第二个,保留这些重要信息之后的就可以定位了
#为什么要把css selector中的内容改短?
#涉及到越多的节点,那么代码的健壮性和可维护性就越差
#因为开发一旦修改页面时,修改了你涉及到的节点,元素就会定位失败
iphone2 = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')",iphone2)
iphone2.click()
#cwh = driver.current_window_handle
#whs = driver.window_handles
#for item in whs:
#    if item == cwh:
#        driver.close()
#    else:
#        driver.switch_to.window(item)

driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()

#添加新地址
driver.find_element_by_name("address[address_name]").send_keys("乌云")
driver.find_element_by_name("address[mobile]").send_keys("15325648752")
#定位下拉框
#driver.find_element_by_css_selector('[value="230000"]').click()
#driver.find_element_by_css_selector('[value="230400"]').click()
#driver.find_element_by_css_selector('[value="230402"]').click()
sheng = driver.find_element_by_id("add-new-area-select")
#下拉框是一种比较特殊的元素.selenium专门为下拉框提供了一种定位方式
#需要把这个元素从webelement类型转化成select类型
#select是selenium专门为我们创建的一个类,用于操作下拉框
#select封装了很多操作下拉框的方法
Select(sheng).select_by_value('230000')
#定位第二个下拉框
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
#定位第三个下拉框
xian = driver.find_elements_by_tag_name("select")[2]
Select(xian).select_by_visible_text("龙沙区")

driver.find_element_by_name("address[address]").send_keys("海淀区")
driver.find_element_by_name("address[zipcode]").send_keys("100086")

driver.find_element_by_class_name("aui_state_highlight").click()

