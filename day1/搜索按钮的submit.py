from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://www.baidu.com'
driver.get(url)

el = driver.find_element_by_id('kw')
el.send_keys('selenium')
time.sleep(5)
el.clear()
el.send_keys('python')

el_sub = driver.find_element_by_id('su')
el_sub.submit()
time.sleep(5)

driver.close()
