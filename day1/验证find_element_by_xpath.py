# link_text 验证带连接的文字
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://bj.58.com'
driver.get(url)

el = driver.find_element_by_xpath(".//[@id]")
el.click()
time.sleep(5)

driver.close()
