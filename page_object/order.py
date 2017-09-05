# coding=utf-8
from __future__ import absolute_import

import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.base_page import BasePage


class Order(BasePage):
    def __init__(self, driver):
        super(Order, self).__init__(driver)

    def __getattribute__(self, item):
        if item == 'new':
            self.wait_datalist_loading()
        return object.__getattribute__(self, item)

    # 通用元素定位信息
    new_button = (By.LINK_TEXT, '我要下单')

    # 新建订单
    def new(self):
        sleep(1)
        self.wait_datalist_loading()
        self.click(*self.new_button)

    def select_adjust(self, adjust):
        buttons = self.get_element(By.CSS_SELECTOR, '#mainBtnContainer button')
        for b in buttons:
            if b.text == adjust:
                b.click()
                break
        self.confirm_dialog()

    def select_type(self, type):
        sel = self.get_element(By.ID, 'order_orderType')
        Select(sel).select_by_value(type)

    def select_adv(self, adv):
        from page_object.selector import Selector
        self.get_element(By.XPATH, '//button[@title="选择"]').click()
        select = Selector(self.driver)
        select.search(adv)
        sleep(1)
        order_productLine = self.get_element(By.ID, 'order_productLine')
        while not order_productLine.text:
            sleep(1)

    def input_amount(self, amount):
        self.input(amount, *(By.ID, 'order_orderAmount'))

    def input_cost(self, cost):
        self.input(cost, *(By.ID, 'order_orderCost'))

    def input_pay_date(self, date):
        try:
            d = int(date)
            date_ = datetime.datetime.now() + datetime.timedelta(days=d)
            date = date_.strftime('%Y-%m-%d')
        except ValueError:
            pass
        self.driver.execute_script('document.getElementById("order_payDate").value="{0}"'.format(date))


    def get_orderno(self):
        input_eles = self.driver.find_elements(By.XPATH,'//input[@name="order[orderno]"]')
        if len(input_eles):
            return input_eles[0].get_attribute('value')
        else:
            return None


    def submit(self, submit):
        self.click(By.XPATH, '//input[@value="{0}"]'.format(submit))
        if submit == '提交':
            sleep(10)
        self.confirm_dialog()
        self.wait_datalist_loading()

    def fill(self, **kwargs):

        dic = {
            '调整': self.select_adjust,
            '类型': self.select_type,
            '广告主': self.select_adv,
            '金额': self.input_amount,
            '成本': self.input_cost,
            '预计支付': self.input_pay_date,
            '提交': self.submit
        }

        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)
