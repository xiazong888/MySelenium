from selenium import webdriver
driver = webdriver.Chrome()

# 设置浏览器显示大小
driver.set_window_size(400,400)
size = driver.get_window_size()

# 设置浏览器所在位置
driver.set_window_position(400,200)

# 关闭当前窗口
driver.close()
# 关闭所有窗口
driver.quit()

