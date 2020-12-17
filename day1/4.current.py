from selenium import webdriver

driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)
# 获取域名和标题
print(driver.current_url)
print(driver.title)

# 自动写文件
driver.get_screenshot_as_file("baidu.jpg")

# 手动写文件
date = driver.get_screenshot_as_png()
with open("baidu2.png","wb") as f:
    f.write(date)


driver.close()