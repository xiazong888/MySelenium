from selenium import webdriver
import unittest
from web_framework.PageObjects.login_page import LoginPage
from web_framework.PageObjects.index_page import IndexPage
from web_framework.TestCases.ModeA import login_datas as LD, common_data as CD
import ddt
import time


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.login_url)
        cls.lg = LoginPage(cls.driver)
        cls.driver.save_screenshot()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def tearDown(self) -> None:
        # 每次执行完一次用例刷新页面
        time.sleep(2)
        self.driver.refresh()

    def test_login_1_success(self):
        self.lg.login(LD.success_data["user"], LD.success_data["pwd"])
        # 断言
        self.assertEqual(IndexPage(self.driver).isExist_loginout_ele())

    @ddt.data(*LD.fail_data)
    def test_login_0_fail(self, data):
        self.lg.login(data["user"], data["pwd"])
        # 断言
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data["check"])
