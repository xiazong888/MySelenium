from selenium import webdriver
# 导入select类
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://www.baidu.com'
driver.get(url)

el_set = driver.find_element_by_link_text('设置')
el_set.click()
time.sleep(3)
el_sou = driver.find_element_by_css_selector('.setpref')
el_sou.click()
time.sleep(2)
# 定位下拉框元素
el_la = driver.find_element_by_id('nr')
time.sleep(3)
# 创建下拉框对象
selobj = Select(el_la)
# 通过index选择
#selobj.select_by_index(0)
#time.sleep(1)
#selobj.select_by_index(1)
#time.sleep(1)
#selobj.select_by_index(2)
#time.sleep(1)
# 通过value值进行选择
selobj.select_by_value('10')
time.sleep(1)
selobj.select_by_value("20")
time.sleep(1)
selobj.select_by_value('50')
time.sleep(1)
# 通过可见文本进行选择
#selobj.deselect_by_visible_text('')
