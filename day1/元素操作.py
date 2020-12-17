from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://bj.58.com/chuzu/?PGTID=0d100000-0000-183b-a3c1-dc16d7a3a243&ClickID=2'
driver.get(url)

el_list = driver.find_elements_by_css_selector("li.house-cell> div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)")
print(el_list)
for el in el_list:
    print("标题:",el.text,"连接：",el.get_attribute("href"))
