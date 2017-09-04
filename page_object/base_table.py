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
            return dict([(v.text, i) for i, v in enumerate(self.ths)])


