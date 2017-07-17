# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By

from .base_page import BasePage


class Selector(BasePage):
    def __init__(self,driver):
        super(Selector, self).__init__(driver)
        self.driver.switch_to.frame(self.get_element(By.CSS_SELECTOR, 'iframe.dialogBodyIfr'))


    def select(self, items):
        first = None
        for item in items:
            item_a = self.driver.find_element(By.LINK_TEXT, item)
            item_i = item_a.find_element(By.XPATH, '../i')
            item_img = item_a.find_element(By.XPATH, '../img')
            if not first:
                first = item_i
            if item == items[-1]:
                item_img.click()
            else:
                item_i.click()

        self.driver.find_element(By.XPATH, '//button[@title="选择"]').click()
        first.click()
        self.confirm()
        sleep(3)

    def search(self,adv):
        search_div=  self.driver.findelement(By.CSS_SELECTOR,'div.search')
        search_input = search_div.find_element(By.TAG_NAME,'input')
        search_input.clear()
        search_input.send_keys(adv)
        search_input.send_keys("Enter")

        tbody = self.driver.find_element(By.TAG_NAME,'tbody')
        input = tbody.find_element(By.TAG_NAME,'input')
        input.click()

        self.confirm()


    def confirm(self):
        self.driver.find_element(By.ID, 'enterBtn').click()

    def cancel(self):
        self.driver.find_element(By.ID, 'cancelBtn').click()
