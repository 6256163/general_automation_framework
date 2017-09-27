# coding=utf-8
from __future__ import absolute_import

import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.base_page import BasePage
from page_object.selector import Selector


class Order(BasePage):
    def __init__(self, driver):
        super(Order, self).__init__(driver)

    def __getattribute__(self, item):
        if item == 'new':
            self.wait_datalist_loading()
        return object.__getattribute__(self, item)

    # 新建订单
    def new(self):
        sleep(1)
        self.wait_datalist_loading()
        self.click(*self.res.order.NEW)

    def select_adjust(self, adjust):
        btn = self.get_element(By.XPATH, '//button[contains(text(), "调整排期和单价")]'.format(adjust))
        self.driver.execute_script("arguments[0].click();", btn)
        self.confirm_dialog()

    def special_flow(self,*args):
        self.click(By.ID, 'order_IsSpecialFlowFlag_0')

    def select_type(self, type):
        sel = self.get_element(*self.res.order.ORDER_TYPE)
        Select(sel).select_by_value(type)

    def select_name(self, name):
        self.input(name, *self.res.order.ORDER_NAME)

    def select_adv(self, adv):
        self.get_element(*self.res.order.ADV).click()
        select = Selector(self.driver)
        select.search(adv)
        sleep(1)
        order_productLine = self.get_element(*self.res.order.PRODUCT_LINE)
        while not order_productLine.text:
            sleep(1)

    def select_AE(self, AE):
        Select(self.get_element(By.ID, 'order_assignAE')).select_by_visible_text(AE)

    def input_amount(self, amount):
        self.input(amount, *self.res.order.AMOUNT)

    def input_cost(self, cost):
        self.input(cost, *self.res.order.COST)

    def input_pay_date(self, date):
        try:
            d = int(date)
            date_ = datetime.datetime.now() + datetime.timedelta(days=d)
            date = date_.strftime('%Y-%m-%d')
        except ValueError:
            pass
        self.driver.execute_script(self.res.order.PAY_DATE.format(date))

    def next(self, next):
        self.click(By.ID, 'next_yes')

    def select_sale(self, sale):
        self.click(By.XPATH, '//button[@data-thickbox-url="/ad/order/getSalesList"]')
        select = Selector(self.driver)
        select.search(sale)
        sleep(1)

    def get_orderno(self):
        input_eles = self.driver.find_elements(*self.res.order.ORDER_NUM)
        if len(input_eles):
            return input_eles[0].get_attribute('value')
        else:
            return None

    def submit(self, submit):
        btn = self.get_element(By.XPATH, '//input[@value = "{0}"]'.format(submit))
        self.driver.execute_script("arguments[0].click();", btn)
        if submit == '提交':
            sleep(30)
        self.confirm_dialog()
        self.wait_datalist_loading()

    def fill(self, **kwargs):

        # 按照字典顺序执行方法
        dic = {
            '调整': self.select_adjust,
            '类型': self.select_type,
            '特批': self.special_flow,
            '名称': self.select_name,
            '广告主': self.select_adv,
            '配合销售': self.select_sale,
            'AE': self.select_AE,
            '金额': self.input_amount,
            '成本': self.input_cost,
            '预计支付': self.input_pay_date,
            '询量组负责人': self.next,
            '提交': self.submit
        }

        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)
