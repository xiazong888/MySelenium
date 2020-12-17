from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from web_framework.PageLocators.loginpage_locators import LoginPageLocator as loc


class SchoolPage:
    def __init__(self, driver):
        self.driver = driver

    # 查询学校
    def get_school(self):
        pass

    # 新建学校
    def new_school(self):
        pass

    # 修改学校
    def update_school(self):
        pass
