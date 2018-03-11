# coding=utf-8
from __future__ import absolute_import

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class BaseTable(BasePage):
    def __init__(self, driver, table=(By.TAG_NAME, 'table'), th=(By.TAG_NAME, 'th')):
        super(BaseTable, self).__init__(driver)
        self.table_loc = table
        self.th_loc = th

    def __getattr__(self, item):
        if item == 'table':
            return self.get_element(*self.table_loc)
        if item == 'ths':
            return self.table.find_elements(*self.th_loc)
        if item == 'columns':
            ths = self.ths
            l = list()
            action = ActionChains(self.driver)
            for i, v in enumerate(ths):
                hover = action.move_to_element(v)
                hover.perform()
                l.append((v.text, i,))
            dic = dict(l)
            return dic
