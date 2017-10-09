# coding=utf-8
from __future__ import absolute_import

import datetime
from time import sleep, time
import re

from selenium.common.exceptions import StaleElementReferenceException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from page_object import store
from page_object.base_table import BaseTable
from .base_page import BasePage


class Table(BaseTable):

    def get_line(self, tr = None):
        if not tr:
            tr = self.table.find_element(By.XPATH, '//tbody//tr')
        return tr.find_elements(By.TAG_NAME, 'td')

    def get_lines(self):
        return self.table.find_elements(By.XPATH, '//tbody//tr')

    def execute(self, operation):
        tr = self.get_lines()[-1] if operation in ['删除', '编辑排期/单价'] else None
        tds = self.get_line(tr=tr)
        btn = tds[self.columns['操作']].find_element(By.XPATH, '//a[@title="{0}"]'.format(operation))
        ActionChains(self.driver).move_to_element(btn).perform()
        btn.click()

        try:
            self.driver.switch_to.alert.accept()
            self.driver.switch_to.default_content()
        except NoAlertPresentException:
            if operation in ['撤销', '提交']:
                self.confirm_dialog()
                self.wait_ajax_loading()

    def get_field(self, field):
        try:
            return self.get_line()[self.columns[field]].text
        except KeyError:
            pass

    def search(self, order):
        if self.get_line()[1].text != order and order:
            input = self.get_element(By.CSS_SELECTOR, 'input.searchTxt')
            input.clear()
            input.send_keys(order)
            input.send_keys(Keys.ENTER)
            self.search_wait(order)

    # verify for data list
    def verify(self, **kwargs):
        tds = self.get_line()
        for (k, v) in kwargs.items():
            actual = tds[self.columns[k]].text
            if actual != v:
                assert False, "Expect: {0}. Actual: {1}".format(v, actual)

    def verify_tg(self, **kwargs):
        for (k,v) in kwargs.items():
            actual = self.get_tg_value(k)
            if k == '分量类型':
                index = v.split(';')
                v = '{0}网盟,{1}外采'.format(
                    '可' if int(index[0]) else '不可',
                    '可' if int(index[1]) else '不可'
                )
            if k == '分量明细':
                num_list = re.findall(r'(\d+)', actual)
                actual = sum(list(map(int, num_list)))
            if str(actual) != str(v):
                assert False, "Expect: {0}. Actual: {1}".format(v, actual)

        # tr = self.table.find_element(By.XPATH,'./tbody/tr[2]')
        # tds = self.get_line(tr=tr)
        # for (k, v) in kwargs.items():
        #     actual = tds[self.columns[k]].text
        #     if k=='分量类型':
        #         index = v.split(';')
        #         v = '{0}网盟,{1}外采'.format(
        #             '可' if int(index[0]) else '不可',
        #             '可' if int(index[1]) else '不可'
        #         )
        #     if k == '分量明细':
        #         num_list = re.findall(r'(\d+)', actual)
        #         store.set_value('component_detail', list(map(int,num_list)))
        #         actual = sum(list(map(int,num_list)))
        #
        #     if str(actual) != str(v):
        #         assert False, "Expect: {0}. Actual: {1}".format(v, actual)

    def get_tg_value(self, k):
        tr = self.table.find_element(By.XPATH, './tbody/tr[2]')
        tds = self.get_line(tr=tr)
        actual = tds[self.columns[k]].text
        return actual

    def search_wait(self, id_):
        sleep(3)
        start= datetime.datetime.now()
        while len(self.table.find_elements(By.XPATH,'//tbody//tr')) != 1 or self.table.find_element(By.XPATH, '//tr[1]//td[2]').text != id_:
            sleep(1)
            end = datetime.datetime.now()
            delta = end - start
            if delta.total_seconds() >10:
                raise TimeoutError


