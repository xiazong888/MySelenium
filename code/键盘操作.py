from selenium import webdriver
# 导入Key类，Key类中包含很多键盘按钮操作
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://cn.bing.com'
driver.get(url)

# 定位到输入框
el = driver.find_element_by_id('sb_form_q')
el.send_keys('selenium')
time.sleep(1)

el.send_keys(Keys.CONTROL,"a")
time.sleep(1)

el.send_keys(Keys.CONTROL,"x")
time.sleep(1)

el.send_keys(Keys.CONTROL,"v")
time.sleep(1)
el.clear()

