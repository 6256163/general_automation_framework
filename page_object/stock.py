# coding=utf-8
from __future__ import absolute_import

from time import sleep

import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage
from .selector import Selector


class Stock(BasePage):
    def __init__(self, driver):
        super(Stock, self).__init__(driver)

    def switch_type(self, type):

        self.wait_ajax_loading()
        if type.upper() == 'CPT':
            stock_type = 'CPT库存报表'
        elif type.upper() == 'CPM':
            stock_type = 'CPM库存报表'
        else:
            stock_type = None
        ul = self.get_element(By.CSS_SELECTOR, 'ul.page_tabs')
        for li in ul.find_elements(By.TAG_NAME, 'li'):
            if li.text == stock_type:
                li.click()
                break
        self.wait_ajax_loading()

    # 选取投放日期
    def select_date(self, dates):
        d = dates.split(';')
        # 点击日期选择器
        self.click(*(By.ID, 'filterDatepicker'))
        # 输入起止时间
        self.input(self.int_to_date(d[0]), *(By.CSS_SELECTOR, 'input.start',))
        self.input(self.int_to_date(d[1]), *(By.CSS_SELECTOR, 'input.end',))
        # 点击确定
        self.click(By.CSS_SELECTOR, 'button.enter')

    def int_to_date(self, num):
        try:
            d = int(num)
            date_ = datetime.datetime.now() + datetime.timedelta(days=d)
            num = date_.strftime('%Y-%m-%d')
        except ValueError:
            pass
        return num

    def select_item(self, items):
        index = int(items.split('/')[0])
        items = items.split('/')[1]
        selecters = self.get_elements(By.CLASS_NAME, 'adr')
        ad_selector = selecters[index].find_element(By.XPATH, '../button')
        for item in items.split(';'):
            ad_selector.click()
            select = Selector(self.driver)
            select.select(item.split('.'))

    def select_port(self, port):
        div = self.get_elements(By.CSS_SELECTOR, 'div.ko_multipleSelectEnhanced')
        sel = div.find_element(By.TAG_NAME, 'select')
        select = Select(sel)
        [select.select_by_visible_text(p) for p in port.split('.')]

    def switch_mode(self, key):

        mode = {
            '下单': 'mode_select',
            '查询': 'mode_view'
        }
        sleep(5)
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format(mode[key])))

    def select_slot(self, slot):
        body = self.get_element(By.CSS_SELECTOR, 'tbody.ui-selectable')
        tr = body.find_elements(By.TAG_NAME, 'tr')[0]
        indexs = slot.split(';')
        for i in indexs:
            tr.find_element(By.XPATH, 'td[@data-index="{0}"]'.format(i)).click()

    def select_order(self,order):
        sel = self.get_elements(By.CSS_SELECTOR,'select.campaign_list')
        select = Select(sel)
        select.select_by_visible_text(order)


    def query(self, **kwargs):
        dic = {
            'type':self.switch_type,
            'date':self.select_date,
            'adr':self.select_item,
            'area':self.select_item,
            'content':self.select_item,
            'port':self.select_port
        }
        for key, value in kwargs.items():
            dic[key](value)

        self.click(*(By.CSS_SELECTOR, 'button.seld'))
        self.wait_ajax_loading()
        sleep(3)


    def add_new(self,**kwargs):
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format('mode_select')))
        dic = {
            'mode':self.switch_mode,
            'slot':self.select_slot,
            'id':self.select_order
        }
        for key, value in kwargs.items():
            dic[key](value)
        createNewBtn = self.get_element(By.ID, 'createNewBtn')
        createNewBtn.click()


