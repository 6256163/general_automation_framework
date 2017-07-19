# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By

from .base_page import BasePage

class Table(BasePage):
    def __init__(self, driver):
        super(Table, self).__init__(driver)
        self.table = self.get_element(By.TAG_NAME,'table')
        self.columns = dict()
        self.init_table()

    def init_table(self):
        ths = self.table.find_elements(By.TAG_NAME,'th')
        self.columns = dict([(v.text,i) for i, v in enumerate(ths)])
        sleep(3)

    def get_line(self):
        tbody = self.get_element(By.TAG_NAME, 'tbody')
        tr = tbody.find_element(By.TAG_NAME, 'tr')
        return tr.find_elements(By.TAG_NAME, 'td')

    def execute(self, operation):
        tds = self.get_line()
        tds[self.columns['操作']].find_element(By.XPATH,'//a[@title="{0}"]'.format(operation)).click()

    def verify(self, **kwargs):
        tds = self.get_line()
        for (k,v) in kwargs.items():
            actual = tds[self.columns[k]].text
            if actual != v:
                return "Expect: {0}. Actual: {1}".format(v,actual)
