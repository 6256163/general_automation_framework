# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_table import BaseTable
from .base_page import BasePage


class Table(BaseTable):

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
        tr = self.get_lines()[-1] if operation in ['删除', '编辑排期/单价'] else None
        tds = self.get_line(tr=tr)
        tds[self.columns['操作']].find_element(By.XPATH, '//a[@title="{0}"]'.format(operation)).click()
        try:
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
        tr = self.get_lines()[-1] if '广告位' in kwargs.keys() else None
        tds = self.get_line(tr= tr)
        for (k, v) in kwargs.items():
            actual = tds[self.columns[k]].text
            if actual != v:
                assert False, "Expect: {0}. Actual: {1}".format(v, actual)


    def search_wait(self, id_):
        sleep(3)
        table = self.get_element(*self.loc)
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        while len(tbody.find_elements(By.TAG_NAME,'tr')) != 1 or tbody.find_element(By.TAG_NAME, 'tr').find_elements(By.TAG_NAME, 'td')[1].text != id_:
            table = self.get_element(*self.loc)
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            sleep(1)


