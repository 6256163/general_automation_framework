# coding=utf-8
from __future__ import absolute_import

from time import sleep

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from executer.operation import Operation


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.ope = Operation(driver=driver)

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
    def get_element(self, *args):
        return self.ope.get_element(*args)

    # 调用接口方法获取多个元素
    def get_elements(self, *args):
        return self.ope.get_elements(*args)

    # 点击元素
    def click(self, *args):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(args)).click()

    # 内容输入
    def input(self, input, *args):
        target = self.get_element(*args)
        target.clear()
        target.send_keys(input)

    # close confirm dialog
    def confirm_dialog(self):
        dialog = self.get_elements(By.XPATH, '//div[@role="dialog"]')
        if len(dialog):
            buttons = dialog[0].find_elements(By.TAG_NAME, 'button')
            for b in buttons:
                if b.text in ["关闭","确定"]:
                    sleep(5)
                    b.click()
                    break

    def wait_ajax_loading(self):
        self.wait_('div.ajaxloading', 'div.ajaxloading_mask')

    def wait_create_table(self):
        self.wait_('div.autoInfoIndicator')

    def wait_datalist_loading(self):
        self.wait_('div.datalist_loading_mask', 'div.datalist_loading')

    def wait_(self, *css_selectors):
        for css in css_selectors:
            while self.driver.find_element(By.CSS_SELECTOR, css):
                while len(self.driver.find_elements(By.CSS_SELECTOR, css)):
                    if not self.driver.find_elements(By.CSS_SELECTOR, css)[0].is_displayed():
                        break
                break