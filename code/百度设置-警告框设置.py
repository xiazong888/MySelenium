from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://www.baidu.com'
driver.get(url)

# 定位到设置
el = driver.find_element_by_link_text('设置')
el.click()

# 定位到搜索设置
el_set = driver.find_element_by_css_selector('.setpref')
el_set.click()
time.sleep(3)
# 定位保存设置按钮
driver.find_element_by_css_selector('.prefpanelgo').click()
time.sleep(2)
# 进入到弹出框用switch_to,或者使用driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()
