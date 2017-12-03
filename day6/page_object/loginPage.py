from selenium.webdriver.common.by import By


class LoginPage:
    #构造方法的作用,实例化LoginPage对象的时候,需要把driver作为参数传进来
    #方便别的方法或属性使用driver
    def __init__(self,driver):
        self.driver = driver

    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"
    #小括号表示元组,元祖中有两个元素,第一个是控件的定位方式,第二个是控件具体的值
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_keys(username)
        #self.driver.find.element(By.ID,"username").send_keys(username)
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()