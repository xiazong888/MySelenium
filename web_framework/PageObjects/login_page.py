from web_framework.PageLocators.loginpage_locators import LoginPageLocator as loc
from web_framework.Common.basepage import BasePage


class LoginPage(BasePage):

    # 登录
    def login(self, user, pwd):
        doc = "登录页面，登录功能"
        self.wait_eleVisible(loc.name_text, doc)
        self.input_text(loc.name_text, doc)
        self.input_text(loc.pwd_text, doc)
        self.click_element(loc.login_but, doc)

    def get_errorMsg_from_loginArea(self):
        doc = "登录页面_获取登录错误提示"
        self.wait_eleVisible(loc.errorMsg_from_loginArea, doc)
        return self.get_text(loc.errorMsg_from_loginArea, doc)
