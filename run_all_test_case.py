import unittest


if __name__ == '__main__':
    # 默认的测试用例加载器,用来寻找所有的符合规则的测试用例
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #执行suite中所有的测试用例
    #TextTestRunner:文本测试用例运行器
    #首字母大写说明是个类,类不能直接调用方法,必须要实例化为对象才能调用方法
    #python中实例化不需要new关键字,直接在类后面加一对小括号
    unittest.TextTestRunner().run(suite)