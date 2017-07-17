# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage

class OrderList(BasePage):
    def __init__(self, driver):
        super(OrderList, self).__init__(driver)

    # 通用元素定位信息
    new = (By.LINK_TEXT, '我要下单')

    # 新建订单
    def new_order(self, **kwargs):
        self.click(self.new)






