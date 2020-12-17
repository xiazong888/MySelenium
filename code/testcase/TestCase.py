import unittest
from Business.Login import Login

class testcase(unittest.TestCase):
    def setUp(self) -> None:
        print('start')
    def tearDown(self) -> None:
        print('end')

    def test_001(self):
        log = Login()
        log.login('diguo168','abcd1234')
        # 获取登录之后的用户名
        date = log.get_text('class_name','hd_login_name')
        # 断言
        self.assertEqual('diguo168',date)
    # 账号密码都不输入
    def test_002(self):
        log = Login()
        log.login('','')
        # 获取登录之后的用户名
        date = log.get_text('id','error_tips')
        # 断言
        self.assertEqual('请输入账号和密码',date)

    # 只输入账号密码不输入
    def test_003(self):
        log = Login()
        log.login('diguo168', '')
        # 获取登录之后的用户名
        date = log.get_text('id', 'error_tips')
        # 断言
        self.assertEqual('请输入密码', date)

    # 只输入账号密码不输入
    def test_004(self):
        log = Login()
        log.login('diguo168', '')
        # 获取登录之后的用户名
        date = log.get_text('id', 'error_tips')
        # 断言
        self.assertEqual('请输入密码111', date)

if __name__ == '__main__':
    unittest.main()