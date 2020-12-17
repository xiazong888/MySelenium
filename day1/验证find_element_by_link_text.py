# link_text 验证带连接的文字
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://bj.58.com'
driver.get(url)

el = driver.find_element_by_link_text('房屋出租')
el.click()
time.sleep(5)

# partial_link_text 与上相比，此方法文本不需要输全
el = driver.find_element_by_partial_link_text('房屋')
el.click()
time.sleep(5)

driver.close()
