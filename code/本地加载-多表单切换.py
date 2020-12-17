from selenium import webdriver
#导入os库，用于获取文件路径
import os
driver = webdriver.Chrome()
# 获取文件访问路径
filePath = 'file:///' + os.path.abspath('example_frame.html')

driver.get(filePath)

#进入第一个表单中
driver.switch_to.frame('itcast_frame1')
#进入第二个表单中
driver.switch_to.frame('itcast_frame2')

#获取输入框的id
el = driver.find_element_by_id('sb_form_q')
el.send_keys('selenium')

#获取搜索按钮的id
el_sub = driver.find_element_by_id('sb_form_go')
el_sub.click()

# 定位一个元素，验证已经到最深表单中
el_search = driver.find_element_by_id('sb_form')
print('还在表单中')

# 退出当前表单
driver.switch_to.default_content()

try:
    el_search = driver.find_element_by_id('sb_form')
except:
    print('已经从表单中退出')
