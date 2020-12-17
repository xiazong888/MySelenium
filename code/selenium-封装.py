from selenium import webdriver
import time
# 封装成一个类

class Common(object):
    #初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def open_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)#隐式等待
    # 封装元素定位
    def locateElement(self,locate_type,value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        return el

    # 操作封装
    def click(self,locate_type,value):
        self.locateElement(locate_type,value).click()
    # 文本输入操作
    def input_date(self,locate_type,value,date):
        el = self.locateElement(locate_type,value)
        el.send_keys(date)
    # 获取定位到的文本内容
    def get_text(self,locate_type,value):
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.text
    # 获取定位到的元素中的标签的属性
    def get_attr(self, locate_type,value,date):
        el = self.locateElement(locate_type,value)
        # 执行点击操作
        return el.get_attribute(date)

    def close_driver(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    con = Common()
    con.open_url('http://www.baidu.com')
    con.input_date('id','kw','selenium')
    con.click('id','su')
    time.sleep(3)

    con.close_driver()