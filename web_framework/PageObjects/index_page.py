from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    # 首页
    def isExist_loginout_ele(self):
        # 定位退出登录元素
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(By.XPATH, "html/body/div[1]/div[1]/a"))
            return True
        except:
            return False
