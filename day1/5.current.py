from selenium import webdriver

driver = webdriver.Chrome()

url = 'http://www.baidu.com'

driver.get(url)

date1 = driver.page_source


with open('baidu.html','wb') as f:
    f.write(date1.encode())

driver.get_screenshot_as_file('baidu3.jpg')
driver.close()