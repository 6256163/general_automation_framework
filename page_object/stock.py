# coding=utf-8
from __future__ import absolute_import

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage
from .selector import Selector


class Stock(BasePage):
    def __init__(self, driver):
        super(Stock, self).__init__(driver)

    def switch_type(self, **kwargs):
        self.wait_ajax_loading()
        if kwargs['type'].upper() == 'CPT':
            stock_type = 'CPT库存报表'
        elif kwargs['type'].upper() == 'CPM':
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
    def select_date(self, **kwargs):
        d = kwargs['date'].split(';')
        # 点击日期选择器
        self.click(*(By.ID, 'filterDatepicker'))
        # 输入起止时间
        self.input(d[0], *(By.CSS_SELECTOR, 'input.start',))
        self.input(d[1], *(By.CSS_SELECTOR, 'input.end',))
        # 点击确定
        self.click(By.CSS_SELECTOR, 'button.enter')

    def select_item(self, index, items=None):
        selecters = self.get_elements(By.CLASS_NAME, 'adr')
        ad_selector = selecters[index].find_element(By.XPATH, '../button')
        for item in items.split(';'):
            ad_selector.click()
            select = Selector(self.driver)
            select.select(item.split('.'))

    def select_port(self, **kwargs):
        div = self.get_elements(By.CSS_SELECTOR, 'div.ko_multipleSelectEnhanced')
        sel = div.find_element(By.TAG_NAME, 'select')
        select = Select(sel)
        [select.select_by_visible_text(p) for p in kwargs['port'].split('.')]

    def switch_mode(self, **kwargs):

        mode = {
            '下单': 'mode_select',
            '查询': 'mode_view'
        }
        sleep(5)
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format(mode[kwargs['mode']])))

    def select_slot(self, **kwargs):
        body = self.get_element(By.CSS_SELECTOR, 'tbody.ui-selectable')
        tr = body.find_elements(By.TAG_NAME, 'tr')[0]
        indexs = kwargs['slot'].split(';')
        for i in indexs:
            tr.find_element(By.XPATH, 'td[@data-index="{0}"]'.format(i)).click()

    def select_order(self,**kwargs):
        sel = self.get_elements(By.CSS_SELECTOR,'select.campaign_list')
        select = Select(sel)
        select.select_by_visible_text(kwargs['order'])


    def query(self, **kwargs):
        if kwargs.get('type', None):
            self.switch_type(**kwargs)
        if kwargs.get('date', None):
            self.select_date(**kwargs)
        if kwargs.get('adr', None):
            self.select_item(0, items=kwargs['adr'])
        if kwargs.get('area', None):
            self.select_item(1, items=kwargs['area'])
        if kwargs.get('content', None):
            self.select_item(2, items=kwargs['content'])
        if kwargs.get('port', None):
            self.select_port(**kwargs)
        self.click(*(By.CSS_SELECTOR, 'button.seld'))
        self.wait_ajax_loading()
        sleep(3)


    def add_new(self,**kwargs):
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format('mode_select')))
        if kwargs.get('slot',None):
            self.select_slot(**kwargs)
        if kwargs.get('id',None):
            self.select_order(**kwargs)
        createNewBtn = self.get_element(By.ID, 'createNewBtn')
        createNewBtn.click()


