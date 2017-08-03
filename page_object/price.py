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

    def fill(self, **kwargs):
        buttons = self.get_elements(By.TAG_NAME, 'button')

        def get_button(btn_text):
            for b in buttons:
                if b.text == btn_text:
                    return b


        if kwargs.get('adv', None):
            get_button('选择广告主').click()
            select = Selector(self.driver)
            select.search(kwargs['adv'])
            sleep(3)

        if kwargs.get('from', None):
            date = kwargs['from']
            try:
                d = int(kwargs['from'])
                date_ = datetime.datetime.now() + datetime.timedelta(days=d)
                date = date_.strftime('%Y-%m-%d')
            except ValueError:
                pass
            self.driver.execute_script('document.getElementById("from").value="{0}"'.format(date))

        if kwargs.get('to', None):
            date = kwargs['to']
            try:
                d = int(kwargs['to'])
                date_ = datetime.datetime.now() + datetime.timedelta(days=d)
                date = date_.strftime('%Y-%m-%d')
            except ValueError:
                pass
            self.driver.execute_script('document.getElementById("to").value="{0}"'.format(date))

        if kwargs.get('adr', None):
            # set adr
            for adr in kwargs['adr'].split(';'):
                get_button('选择广告位').click()
                select = Selector(self.driver)
                select.select(adr.split('.'))

        if kwargs.get('area', None):
            for area in kwargs['area'].split(';'):
                get_button('选择地域').click()
                selector = Selector(self.driver)
                selector.select(area.split('.'))


        if kwargs.get('port', None):
            table = Table(self.driver)
            selects = table.table.find_elements(By.TAG_NAME,'select')
            for port, sel in zip(kwargs['port'].split(';'),selects):
                select = Select(sel)
                [select.select_by_visible_text(p) for p in port.split('.')]

        if kwargs.get('price', None):
            table = Table(self.driver)
            tds = table.table.find_elements(By.CSS_SELECTOR,'td.put_price_set')
            # adr
            for price, td in zip(kwargs['price'].split(';'),tds):
                for p, input in zip(price.split('.'),td.find_elements(By.TAG_NAME,'input')):
                    input.clear()
                    input.send_keys(p)

        if kwargs.get('type', None):
            table = Table(self.driver)
            for i, ad_type in enumerate(kwargs['type'].split(';')):
                if ad_type == '贴片':
                    input = table.table.find_element(By.ID, 'paster-' + str(i))
                else:
                    input = table.table.find_element(By.ID, 'hard-' + str(i))
                input.click()

        if kwargs.get('submit', None):
            self.click(By.XPATH, "//input[@value='{0}']".format(kwargs['submit']))
            self.confirm_dialog()
