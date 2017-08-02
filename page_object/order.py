# coding=utf-8
from __future__ import absolute_import
import datetime
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
        self.wait_datalist_loading()

    # 通用元素定位信息
    new_button = (By.LINK_TEXT, '我要下单')

    # 新建订单
    def new(self):
        self.wait_datalist_loading()
        self.click(*self.new_button)


    def fill(self, **kwargs):
        if kwargs.get('adjust',None):
            div = self.get_element(By.ID,'mainBtnContainer')
            buttons = div.find_elements(By.TAG_NAME,'button')
            for b in buttons:
                if b.text == kwargs['adjust']:
                    b.click()
                    break
            self.confirm_dialog()

        # fill per_order info
        if kwargs.get('type', None):
            sel = self.get_element(By.ID, 'order_orderType')
            Select(sel).select_by_value(kwargs['orderType'])

        if kwargs.get('adv', None):
            self.get_element(By.XPATH, '//button[@title="选择"]').click()
            select = Selector(self.driver)
            select.search(kwargs['adv'])
            sleep(3)

        # fill order info
        if kwargs.get('amount', None):
            self.input(kwargs['amount'], *(By.ID, 'order_orderAmount'))

        if kwargs.get('cost', None):
            self.input(kwargs['cost'], *(By.ID, 'order_orderCost'))

        if kwargs.get('pay_date', None):
            date = kwargs['pay_date']
            try:
                d = int(kwargs['pay_date'])
                date_ = datetime.datetime.now() + datetime.timedelta(days=d)
                date = date_.strftime('%Y-%m-%d')
            except ValueError:
                pass
            self.driver.execute_script('document.getElementById("order_payDate").value="{0}"'.format(date))

        # final operation
        if kwargs['submit']:
            self.click(By.XPATH, '//input[@value="{0}"]'.format(kwargs['submit']))
            self.confirm_dialog()

    def execute(self, **kwargs):
        table = Table(self.driver)
        table.execute(kwargs['operation'])
        self.confirm_dialog()
        if  kwargs['operation'] == '撤销':
            self.wait_ajax_loading()




