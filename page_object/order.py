# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.selector import Selector
from .base_page import BasePage

class Order(BasePage):
    def __init__(self, driver):
        super(Order, self).__init__(driver)

    # 通用元素定位信息
    new = (By.LINK_TEXT, '我要下单')

    # 新建订单
    def new_order(self, **kwargs):
        self.click(*self.new)
        self.wait_ajax_loading()


    def per_order(self, **kwargs):
        if  kwargs['type']:
            sel = self.get_element(By.ID,'order_orderType')
            Select(sel).select_by_value(kwargs['orderType'])

        if kwargs['order_advId']:
            ad_input = self.get_element(By.ID,'order_advId')
            ad_button = ad_input.find_element(By.XPATH,'../button').click()
            select = Selector(self.driver)
            select.search(kwargs['adv'])


        if kwargs['operation']:
            self.click(By.XPATH,'//input[@value="{0}"]'.format(kwargs['operation']))





