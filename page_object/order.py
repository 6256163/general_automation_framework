# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.selector import Selector
from page_object.table import Table
from .base_page import BasePage

class Order(BasePage):
    def __init__(self, driver):
        super(Order, self).__init__(driver)
        self.wait_mask()

    # 通用元素定位信息
    new_button = (By.LINK_TEXT, '我要下单')

    # 新建订单
    def new(self, **kwargs):
        self.click(*self.new_button)
        self.wait_ajax_loading()


    def fill(self, **kwargs):
        if kwargs.get('type',None):
            sel = self.get_element(By.ID,'order_orderType')
            Select(sel).select_by_value(kwargs['orderType'])

        if kwargs.get('adv',None):
            self.get_element(By.XPATH,'//button[@title="选择"]').click()
            select = Selector(self.driver)
            select.search(kwargs['adv'])
            sleep(3)


        if kwargs['operation']:
            self.click(By.XPATH,'//input[@value="{0}"]'.format(kwargs['operation']))
            dialog = self.get_element(By.XPATH,'//div[@role="dialog"]')
            buttons = dialog.find_elements(By.TAG_NAME,'button')
            for b in buttons:
                if b.text == "关闭":
                    sleep(5)
                    b.click()
                    break



    def execute(self, **kwargs):
        table = Table(self.driver)
        table.execute(kwargs['operation'])


    def verify_list(self, **kwargs):
        table = Table(self.driver)
        return table.verify(**kwargs)