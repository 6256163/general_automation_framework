# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class Table(BasePage):
    def __init__(self, driver):
        super(Table, self).__init__(driver)
        self.table = self.get_element(By.TAG_NAME,'table')
        self.columns = dict()
        self.init_table()

    def init_table(self):
        ths = self.table.find_elements(By.TAG_NAME,'th')
        try:
            self.columns = dict([(v.text,i) for i, v in enumerate(ths)])
        except StaleElementReferenceException:
            pass
        sleep(3)

    def get_line(self):
        tbody = self.get_element(By.TAG_NAME, 'tbody')
        tr = tbody.find_element(By.TAG_NAME, 'tr')
        return tr.find_elements(By.TAG_NAME, 'td')

    def get_lines(self):
        tbody = self.get_element(By.TAG_NAME, 'tbody')
        return tbody.find_elements(By.TAG_NAME, 'tr')

    def execute(self, operation):
        tds = self.get_line()
        tds[self.columns['操作']].find_element(By.XPATH,'//a[@title="{0}"]'.format(operation)).click()

    def get_field(self, field):
        return self.get_line()[self.columns[field]].text

    def search(self,order):
        input = self.get_element(By.CSS_SELECTOR,'input.searchTxt')
        input.clear()
        input.send_keys(order)
        input.send_keys(Keys.ENTER)
        sleep(3)
        self.wait_datalist_loading()

    def verify(self, **kwargs):
        for key in ['order','price']:
            if kwargs.get(key,None):
                self.search(kwargs[key])
                kwargs.pop(key)
        tds = self.get_line()
        for (k,v) in kwargs.items():
            actual = tds[self.columns[k]].text
            if actual != v:
                return "Expect: {0}. Actual: {1}".format(v,actual)
