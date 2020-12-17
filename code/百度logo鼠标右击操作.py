from selenium import webdriver
# 导出动作连接
from selenium.webdriver import ActionChains

# 开浏览器
driver = webdriver.Chrome()
url = 'http://www.baidu.com'

driver.get(url)

# 定位到百度的logo
el_name = driver.find_element_by_css_selector('#lg > img:nth-child(1)')
# 鼠标右击操作,需要将操作的元素定位出来，传入到响应的动作中,调用perform方法执行该动作（重点）
ActionChains(driver).context_click(el_name).perform()
# 双击操作
ActionChains(driver).double_click(el_name).perform()
