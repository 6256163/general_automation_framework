# coding=utf-8
from __future__ import absolute_import

from time import sleep

from selenium.webdriver.common.by import By

from .base_page import BasePage
from .selector import Selector


class Stock(BasePage):
    def __init__(self, driver):
        super(Stock, self).__init__(driver)

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

    def open_selector(self, **kwargs):
        selecters = self.get_elements(By.CLASS_NAME, 'adr')
        ad_selector = selecters[int(kwargs['index'])].find_element(By.XPATH, '../button')
        ad_selector.click()

    def select_item(self, **kwargs):
        select = Selector(self.driver)
        select.select(kwargs['items'].split('.'))

    def select_confirm(self):
        select = Selector(self.driver)
        select.confirm()

    def query(self):
        self.click(*(By.CSS_SELECTOR, 'button.seld'))
        self.wait_create_table()

    def switch_mode(self, **kwargs):

        mode = {
            '下单': 'mode_select',
            '查询': 'mode_view'
        }

        self.wait_mask()
        self.click(*(By.XPATH,'//label[@for="{0}"]'.format(mode[kwargs['mode']])))

    def choose_date(self,**kwargs):
        body = self.get_element(By.CSS_SELECTOR,'tbody.ui-selectable')
        tr = body.find_elements(By.TAG_NAME,'tr')[0]
        indexs = kwargs['index'].split(';')
        for i in indexs:
            tr.find_element(By.XPATH,'td[@data-index="{0}"]'.format(i)).click()
        createNewBtn = self.get_element(By.ID,'createNewBtn')
        createNewBtn.click()
