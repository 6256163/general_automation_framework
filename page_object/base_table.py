# coding=utf-8
from __future__ import absolute_import

from time import sleep

from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from executer.operation import Operation
from page_object.base_page import BasePage


class BaseTable(BasePage):
    def __init__(self, driver, table=(By.TAG_NAME, 'table'), th=(By.NAME, 'th')):
        super(BaseTable, self).__init__(driver)
        self.table_loc = table
        self.th_loc = th
        self.table = None
        self.ths = None  # self.table.find_element(*th) if th else th
        self.columns = dict()

    def __getattribute__(self):
        if not self.table:
            self.table = self.get_element(*self.table_loc)
            self.ths = self.table.find_element(*self.th_loc)
            self.init_table()

        self.columns = dict([(v.text, i) for i, v in enumerate(self.ths)])
        sleep(3)
