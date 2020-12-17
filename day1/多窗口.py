from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://bj.58.com/'
driver.get(url)

el = driver.find_element_by_link_text('租房')
print("点击之前的身份证列表:",driver.window_handles)
print('点击之前的url：',driver.current_url)
print('点击之前的标题：',driver.title)
el.click()
print("点击之后的身份证列表:",driver.window_handles)
print('点击之后的url：',driver.current_url)

hadles_list = driver.window_handles
driver.switch_to.window(hadles_list[1])

print('点击之后的标题：',driver.title)