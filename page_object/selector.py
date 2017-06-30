# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Selector(BasePage):
    def __init__(self):
        selector_ifr = self.get_element(By.CSS_SELECTOR, 'iframe.dialogBodyIfr')
        

    def select(self, items):
        for item in items:
            item_a = self.get_element(By.LINK_TEXT, item)
            item_li = item_a.find_element(By.XPATH, '.')
            item_li.click()

    def
