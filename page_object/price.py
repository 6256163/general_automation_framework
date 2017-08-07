# coding=utf-8
import pymysql
import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object.base_page import BasePage
from page_object.selector import Selector
from page_object.table import Table


class Price(BasePage):
    def __init__(self, driver):
        super(Price, self).__init__(driver)
        self.wait_datalist_loading()

    new_button = (By.LINK_TEXT, '新增价格政策')

    def new(self):
        self.wait_datalist_loading()
        self.click(*self.new_button)

    def get_button(self, btn_text):
        buttons = self.get_elements(By.TAG_NAME, 'button')
        for b in buttons:
            if b.text == btn_text:
                return b

    def select_adv(self,adv):
        self.get_button('选择广告主').click()
        select = Selector(self.driver)
        select.search(adv)
        sleep(3)

    def select_date(self,date):
        dates = date.split(';')
        for i, d in enumerate(dates):
            try:
                d = int(d)
                date_ = datetime.datetime.now() + datetime.timedelta(days=d)
                date = date_.strftime('%Y-%m-%d')
            except ValueError:
                pass
            dic = {
                0:'from',
                1:'to'
            }
            self.driver.execute_script('document.getElementById("{0}").value="{1}"'.format(dic[i],date))

    def select_adr(self,adr):
        for adr in adr.split(';'):
            self.get_button('选择广告位').click()
            select = Selector(self.driver)
            select.select(adr.split('.'))

    def select_area(self,area):
        for area in area.split(';'):
            self.get_button('选择地域').click()
            selector = Selector(self.driver)
            selector.select(area.split('.'))

    def select_port(self, port):
        table = Table(self.driver)
        selects = table.table.find_elements(By.TAG_NAME, 'select')
        for port, sel in zip(port.split(';'), selects):
            select = Select(sel)
            [select.select_by_visible_text(p) for p in port.split('.')]

    def input_price(self,price):
        table = Table(self.driver)
        tds = table.table.find_elements(By.CSS_SELECTOR, 'td.put_price_set')
        # adr
        for price, td in zip(price.split(';'), tds):
            for p, input in zip(price.split('.'), td.find_elements(By.TAG_NAME, 'input')):
                input.clear()
                input.send_keys(p)

    def select_type(self, type):
        table = Table(self.driver)
        for i, ad_type in enumerate(type.split(';')):
            if ad_type == '贴片':
                input = table.table.find_element(By.ID, 'paster-' + str(i))
            else:
                input = table.table.find_element(By.ID, 'hard-' + str(i))
            input.click()

    def submit(self,submit):
        self.click(By.XPATH, "//input[@value='{0}']".format(submit))
        self.confirm_dialog()

    def fill(self, **kwargs):
        dic = {
            'adv':self.select_adv,
            'date':self.select_date,
            'adr':self.select_adr,
            'area':self.select_area,
            'port':self.select_port,
            'price':self.input_price,
            'type':self.select_type,
            'submit':self.submit,
        }

        for key, value in kwargs.items():
            dic[key](value)

