from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'http://renren.com'
driver.get(url)

el_name = driver.find_element_by_name('email')
el_name.send_keys('账号')

el_pwd = driver.find_element_by_name('password')
el_pwd.send_keys('密码')

el_sub = driver.find_element_by_id('login')
el_sub.click()
time.sleep(5)
driver.close()

#循环往后翻页
for i in range(10):
    # 通过class属性值定位到下一页
    el_next = driver.find_element_by_class_name('abc')
    el_next.click()
    time.sleep(5)