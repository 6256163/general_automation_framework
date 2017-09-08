# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class Selector(BasePage):
    def __init__(self,driver):
        super(Selector, self).__init__(driver)
        self.driver.switch_to.default_content()
        ifrs = self.driver.find_elements(By.TAG_NAME, 'iframe')
        for ifr in ifrs:
            if ifr.size['width'] != 0:
                self.driver.switch_to.frame(ifr)
                break

    def clear(self):
        self.driver.find_element(By.XPATH, '//button[@title="清除"]').click()

    def select(self, items):
        first = None
        if items == ['']:
            self.driver.find_element(By.XPATH, '//button[@title="清空"]').click()
            items.pop()
        for item in items:
            item_a = self.get_element(By.LINK_TEXT, item)
            item_i = item_a.find_element(By.XPATH, '../i')
            if not first:
                first = item_i
            if item == items[-1]:
                item_img = item_a.find_element(By.XPATH, '../img')
                item_img.click()
            else:
                item_i.click()

        self.driver.find_element(By.XPATH, '//button[@title="选择"]').click()
        self.confirm()
        sleep(3)

    def search(self,adv):
        search_div=  self.driver.find_element(By.CSS_SELECTOR,'div.search')
        search_input = search_div.find_element(By.TAG_NAME,'input')
        search_input.clear()
        search_input.send_keys(adv)
        search_input.send_keys(Keys.ENTER)
        self.get_element(By.XPATH,'//tbody[last()]/tr/td[3][contains(text(),"{0}")]'.format(adv))
        self.confirm()


    def confirm(self):
        self.driver.find_element(By.ID, 'enterBtn').click()

    def cancel(self):
        self.driver.find_element(By.ID, 'cancelBtn').click()
