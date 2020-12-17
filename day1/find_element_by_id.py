from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'https://qunar.com'
driver.get(url)

# 练习find_element_by_id
time.sleep(2)
el = driver.find_element_by_id('__link_travel__')

el.click()

driver.close()

