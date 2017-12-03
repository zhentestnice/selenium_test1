import unittest

import time

from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connectDb


class Zhuce_test(MyTestCase):
    def test_zhuce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("zhentest3")
        driver.find_element_by_name("password").send_keys("1234qwer")
        driver.find_element_by_name("userpassword2").send_keys("1234qwer")
        driver.find_element_by_name("mobile_phone").send_keys("18210273433")
        driver.find_element_by_name("email").send_keys("tianzhen113@163.com")
        driver.find_element_by_class_name("reg_btn").click()
        #检查数据库中新增的用户名和我们输入的是否一致
        expected = "zhentest3"
        time.sleep(3)
        actual = connectDb()[1]
        self.assertEqual(expected,actual)
        print(connectDb()[1])