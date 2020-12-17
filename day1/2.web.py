from selenium import webdriver
import time
# 创建浏览器对象
driver = webdriver.Chrome()

driver.set_window_size(1000,700)
driver.set_window_position(250,0)
#访问百度

url = "http://www.baidu.com"
driver.get(url)

url = "http://zhuanlan.zhihu.com"

driver.get(url)

time.sleep(2)
#后退
driver.back()
time.sleep(2)
#前进
driver.forward()