from selenium import webdriver
import time
# 创建浏览器对象
driver = webdriver.Chrome()

driver.set_window_size(1000,700)
driver.set_window_position(250,0)
#访问百度

url1 = "http://www.baidu.com"
driver.get(url1)
print(driver.current_url)

url2 = "http://zhuanlan.zhihu.com"
driver.get(url2)
print(driver.current_url)

#后退
driver.back()
print("后退到",driver.current_url)
#前进
driver.forward()
print("前进到",driver.current_url)