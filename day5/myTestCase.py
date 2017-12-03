import unittest
import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()