# coding=utf-8
from __future__ import absolute_import

from time import sleep

import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object import store
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
        self.input(int_to_date(d[0]), *(By.CSS_SELECTOR, 'input.start',))
        self.input(int_to_date(d[1]), *(By.CSS_SELECTOR, 'input.end',))
        # 点击确定
        self.click(By.CSS_SELECTOR, 'button.enter')


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
        sel = div[0].find_element(By.TAG_NAME, 'select')
        select = Select(sel)
        [select.select_by_visible_text(p) for p in port.split('.')]

    def switch_mode(self, key):

        mode = {
            '下单': 'mode_select',
            '查询': 'mode_view'
        }
        sleep(5)
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format(mode[key])))

    mode = {
        '下单': 'mode_select',
        '查询': 'mode_view'
    }

    def select_slot(self, slot):
        sleep(5)
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format('mode_select')))
        body = self.get_element(By.CSS_SELECTOR, 'tbody.ui-selectable')
        tr = body.find_elements(By.TAG_NAME, 'tr')[0]
        indexs = slot.split(';')
        try:
            key = int(indexs[-1])
        except ValueError:
            key = indexs.pop()
        slot_list = []
        for i in indexs:
            cell = tr.find_element(By.XPATH, 'td[@data-index="{0}"]'.format(i))
            slot_list.append(cell.text)
            cell.click()
        if type(key) == 'str':
            store.set_value(key, slot_list)

    def select_order(self, order):
        sel = self.get_element(By.CSS_SELECTOR, 'select.campaign_list')
        select = Select(sel)
        select.select_by_visible_text(order)

    def submit(self, submit):

        map = {
            '加入': 'createNewBtn',
            '编辑': 'editOneBtn'
        }
        btn = self.get_element(By.ID, map[submit])
        btn.click()

    def query(self, **kwargs):
        dic = {
            'type': self.switch_type,
            'date': self.select_date,
            'adr': self.select_item,
            'area': self.select_item,
            'content': self.select_item,
            'port': self.select_port
        }
        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)

        self.click(*(By.CSS_SELECTOR, 'button.seld'))
        self.wait_ajax_loading()
        sleep(3)

    def cpm_set(self,cpm):
        self.input(cpm, By.CSS_SELECTOR, 'div.cpm_set input')
        self.click(By.CSS_SELECTOR, 'div.btnbar button.enterBtn')

    def add_new(self, **kwargs):
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format('mode_select')))
        dic = {
            'slot': self.select_slot,
            'order': self.select_order,
            'submit': self.submit,
            'cpm':self.cpm_set
        }
        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)






def int_to_date(num):
    try:
        d = int(num)
        date_ = datetime.datetime.now() + datetime.timedelta(days=d)
        num = date_.strftime('%Y-%m-%d')
    except ValueError:
        pass
    return num