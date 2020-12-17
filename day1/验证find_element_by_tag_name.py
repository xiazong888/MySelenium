# 标签定位
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://cn.bing.com'
driver.get(url)
# 通过标签定位，该元素要么唯一，要么是第一个
el = driver.find_element_by_tag_name('input')
el.send_keys('selenium')

el_sub = driver.find_element_by_id('sb_from_go')
el_sub.click()

time.sleep(5)

driver.close()