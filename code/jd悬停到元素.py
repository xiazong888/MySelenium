from selenium import webdriver
# 导出动作链类
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://www.jd.com'
driver.get(url)

# 获取分组类元素
el_list = driver.find_elements_by_class_name('cate_menu_item')

for el in el_list:
    ActionChains(driver).move_to_element(el).perform()
    time.sleep(1)



