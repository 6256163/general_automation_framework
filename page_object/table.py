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


    def execute(self, operation):
        tbody = self.get_element(By.TAG_NAME,'tbody')
        tr = tbody.find_element(By.TAG_NAME,'tr')
        tds = tr.find_elements(By.TAG_NAME,'td')
        tds[-1].find_element(By.XPATH,'//a[@title="{0}"]'.format(operation)).click()

