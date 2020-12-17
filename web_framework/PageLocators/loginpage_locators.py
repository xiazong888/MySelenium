from selenium.webdriver.common.by import By


# 元素定位
class LoginPageLocator:
    # 用户名
    name_text = (By.XPATH, ".//*[@id='txtUserName']")
    # 密码
    pwd_text = (By.XPATH, ".//*[@id='txtPassword']")
    # 登录按钮
    login_but = (By.XPATH, ".//*[@id='loginForm']/a")
    # 错误提示
    errorMsg_from_loginArea = (By.XPATH, '//*[@id="msg"]/div/strong')
