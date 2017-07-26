# coding=utf-8
from __future__ import absolute_import

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
        try:
            self.get_element(*args).click()
        except WebDriverException:
            self.get_element(*args).click()
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(args)).click()

    # 内容输入
    def input(self, input, *args):
        target = self.get_element(*args)
        target.clear()
        target.send_keys(input)

    def wait_ajax_loading(self):
        try:
            while self.driver.find_element(By.CSS_SELECTOR, 'div.ajax_loading').is_displayed() \
                    or self.driver.find_element(By.CSS_SELECTOR, 'div.ajaxloading_mask').is_displayed():
                pass
        except NoSuchElementException:
            pass


    def wait_create_table(self):
        try:
            while self.driver.find_element(By.CSS_SELECTOR, 'div.autoInfoIndicator').is_displayed():
                pass
        except NoSuchElementException:
            pass

    def wait_mask(self):
        try:
            while self.driver.find_element(By.CSS_SELECTOR, 'div.datalist_loading_mask').is_displayed() \
                    or self.driver.find_element(By.CSS_SELECTOR, 'div.ajaxloading_mask').is_displayed():
                pass
        except NoSuchElementException:
            pass
