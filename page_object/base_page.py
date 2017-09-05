# coding=utf-8
from __future__ import absolute_import

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 调用方法
    def perform(self, func, **kwargs):
        """
        :param func: 方法名
        :param kwargs: 被调用方法的参数
        :return: None
        """
        self.__getattribute__(func)(**kwargs)

    # 打开页面
    def open_page(self, url):
        """
        :param url: 页面地址
        :return: None
        """
        self.driver.get(url=url)

    # 返回当前页面标题
    def get_title(self):
        return self.driver.title

    # 调用接口方法获取单个元素
    def get_element(self, by, value):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(by,value).is_displayed())
            return self.driver.find_element(by,value)
        except NoSuchElementException(msg=u"Fail to find element: {0} {1}".format(by, value)):
            assert False, u"Fail to find element: {0} {1}".format(by, value)

    # 调用接口方法获取多个元素
    def get_elements(self, by, value):
        return self.driver.find_elements(by, value)

    # 点击元素
    def click(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value,))).click()

    # 内容输入
    def input(self, input, by, value):
        target = self.get_element(by, value)
        target.clear()
        target.send_keys(input)

    # close confirm dialog
    def confirm_dialog(self):
        dialog = self.get_elements(By.XPATH, '//div[@role="dialog"]')
        if len(dialog):
            buttons = dialog[0].find_elements(By.TAG_NAME, 'button')
            for b in buttons:
                if b.text in ["关闭","确定"]:
                    b.click()
                    break

    def wait_ajax_loading(self):
        self.wait_('div.ajaxloading', 'div.ajaxloading_mask')

    def wait_create_table(self):
        self.wait_('div.autoInfoIndicator')

    def wait_datalist_loading(self):
        self.wait_('div.datalist_loading_mask', 'div.datalist_loading')

    def wait_grid_table_loading(self):
        self.wait_('div#grid_table_loading')

    def wait_(self, *css_selectors):
        for css in css_selectors:
            while self.driver.find_element(By.CSS_SELECTOR, css):
                while len(self.driver.find_elements(By.CSS_SELECTOR, css)):
                    try:
                        if not self.driver.find_element(By.CSS_SELECTOR, css).is_displayed():
                            break
                    except Exception as e:
                        pass
                break