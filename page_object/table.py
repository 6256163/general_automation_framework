# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class Table(BasePage):
    def __init__(self, driver, loc=(By.TAG_NAME, 'table')):
        super(Table, self).__init__(driver)
        self.loc = loc
        self.columns = dict()
        self.init_table()

    def init_table(self):
        self.table = self.get_element(*self.loc)
        ths = self.table.find_elements(By.TAG_NAME, 'th')
        self.columns = dict([(v.text, i) for i, v in enumerate(ths)])
        sleep(3)

    def get_line(self, tr = None):
        if not tr:
            table = self.get_element(*self.loc)
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            tr = tbody.find_element(By.TAG_NAME, 'tr')
        return tr.find_elements(By.TAG_NAME, 'td')

    def get_lines(self):
        table = self.get_element(*self.loc)
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        return tbody.find_elements(By.TAG_NAME, 'tr')

    def execute(self, operation):
        tds = self.get_line()
        tds[self.columns['操作']].find_element(By.XPATH, '//a[@title="{0}"]'.format(operation)).click()
        try:
            self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
            self.driver.switch_to.default_content()
        except NoAlertPresentException:
            self.confirm_dialog()
            if operation in ['撤销', '提交']:
                self.wait_ajax_loading()

    def get_field(self, field):
        try:
            self.init_table()
            return self.get_line()[self.columns[field]].text
        except KeyError:
            pass
    def search(self, order):
        if self.get_line()[1].text != order:
            input = self.get_element(By.CSS_SELECTOR, 'input.searchTxt')
            input.clear()
            input.send_keys(order)
            input.send_keys(Keys.ENTER)
            self.search_wait(order)

    def verify(self, **kwargs):
        tds = self.get_line() if filter(lambda page: page in kwargs.keys(), ['order', 'price']) \
            else self.get_line(self.get_lines[-1])
        for (k, v) in kwargs.items():
            if k in ['order', 'price']:
                continue
            actual = tds[self.columns[k]].text
            if actual != v:
                return "Expect: {0}. Actual: {1}".format(v, actual)


    def search_wait(self, id_):
        sleep(3)
        table = self.get_element(*self.loc)
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        while len(tbody.find_elements(By.TAG_NAME,'tr')) != 1 or tbody.find_element(By.TAG_NAME, 'tr').find_elements(By.TAG_NAME, 'td')[1].text != id_:
            table = self.get_element(*self.loc)
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            sleep(1)


