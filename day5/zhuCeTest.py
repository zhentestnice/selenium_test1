#有了myTestCase以后,在写测试用例,就不需要重写setup和teardown方法了
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    """注册模块测试用例"""
    def test_zhuce(self):
        """打开正常"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #driver.current_url #用来获取当前浏览器URL
        actual = driver.title       #用来获取当前浏览器中标签页的title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        base_path = os.path.dirname(__file__)
        path = base_path.replace('day5','report/image/')
        print(base_path,path)
        driver.get_screenshot_as_file(path + "zhuce.png")  #截取整个浏览器图片
        self.assertEqual(actual,expected)
