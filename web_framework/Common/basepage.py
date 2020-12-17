# 封装基本函数--执行日志，异常处理，失败截图
# 所有页面的公共部分
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=""):
        '''
        :param locator:元素定位，元素定位类型：元组（元素定位类型，元素定位方式）
        :param times:等待时长
        :param poll_frequency:休眠时间的间隔（步长）时间，默认为 0.5 秒
        :param doc:模块名_页面名_操作名
        :return:
        '''
        logging.info("等待元素 {0} 可见".format(locator))
        try:
            # 开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(
                EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("等待结束，等待时长为{}")
        except:
            logging.exception("等待元素可见失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素可见
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("查找元素{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0} 点击元素{1}".format(locator, doc))
        # 点击
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0} 输入元素{1}".format(locator, doc))
        # 点击
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def element_atttribute(self, locator, attr, doc=""):  # attr:属性名称
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素属性失败！")
            # 截图
            self.save_screenshot(doc)
            raise

    # alert 处理
    def alert_action(self, action='accept'):
        pass

    # iframe切换
    def switch_iframe(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    def save_screenshot(self, name):
        # 图片名称：模块名_页面名称_操作名称_时间(年月日时分秒).jpg
        file_name = "截屏存放的路径" + "文件名格式".format(name, )  # 不完整
        self.driver.save_screenshot("截屏存放的路径" + file_name)
        logging.info("截取网页成功，文件路径为:{}".format(file_name))
