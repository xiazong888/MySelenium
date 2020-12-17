from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

url = 'http://www.baidu.com'
driver.get(url)

time.sleep(6)
el = driver.find_element(By.ID,'kw')
#el = driver.find_element_by_id('kw')
el.send_keys('传智博客')

el_sub = driver.find_element(By.ID,'su')
el_sub.click()

time.sleep(5)

driver.close()