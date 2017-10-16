# coding=utf-8
from __future__ import absolute_import

from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_object.resources.resources import Resources


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.res = Resources()


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
            e = self.driver.find_element(by,value)
            self.driver.execute_script("window.scroll(0, {0})".format(e.location['y']))
            return e
        except NoSuchElementException as e:
            assert False, u"Fail to find element: {0} {1}".format(by, value)
        except TimeoutException as e:
            assert False, u"Timeout to find element: {0} {1}".format(by, value)

    # 调用接口方法获取多个元素
    def get_elements(self, by, value):
        return self.driver.find_elements(by, value)

    # 点击元素
    def click(self, by, value):
        # self.driver.execute_script("arguments[0].click();", self.get_element(by,value))
        #ac = ActionChains(self.driver)
        #ac.move_to_element(self.get_element(by,value)).perform()
        self.get_element(by,value)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value,))).click()
        except Exception as e:
            assert False, e

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
        self.wait_('div.ajaxloading_mask')

    def wait_create_table(self):
        self.wait_('div.autoInfoIndicator')

    def wait_datalist_loading(self):
        self.wait_('div.datalist_loading_mask')

    def wait_grid_table_loading(self):
        self.wait_('div#grid_table_loading')

    def wait_(self, *css_selectors):
        for css in css_selectors:
            sleep(3)
            while len(self.get_elements(By.CSS_SELECTOR, css)):
                try:
                    if not self.get_elements(By.CSS_SELECTOR, css)[0].is_displayed():
                        break
                except Exception as e:
                    pass
            break