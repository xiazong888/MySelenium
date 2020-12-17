#网站登录有防爬虫设置，用表单定位
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://126.com/'
driver.get(url)

#获取表单
#driver.switch_to.frame('x-URS-iframe')
#定位到密码登录文字链接
link_text = driver.find_element_by_link_text('密码登录')
link_text.click()
#获取表单
driver.switch_to.frame('#x-URS-iframe1584204387831\.9216')
#'#x-URS-iframe1584204839793\.5427'
#定位到登录框
el_user = driver.find_element_by_name('email')
el_user.send_keys('xiacj1')

#定位到密码框
el_pwd = driver.find_element_by_name('password')
el_pwd.send_keys('@WSX3edc')

#定位到登录按钮
el_sub = driver.find_element_by_id('dologin')
el_sub.click()
time.sleep(5)



