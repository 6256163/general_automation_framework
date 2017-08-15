# coding=utf-8
from __future__ import absolute_import
import datetime
from selenium.webdriver.common.by import By

from .stock import int_to_date
from .base_page import BasePage


class TG(BasePage):
    def __init__(self,driver):
        super(TG, self).__init__(driver)
        self.driver.switch_to.default_content()
        ifrs = self.driver.find_elements(By.CSS_SELECTOR, 'iframe.dialogBodyIfr')
        for ifr in ifrs:
            if ifr.size['width'] != 0:
                self.driver.switch_to.frame(ifr)
                break


    def adslot(self, ads):
        actual = self.driver.find_element(By.CSS_SELECTOR,'td.col-adslot').text
        if actual!= ads:
            assert False, "Expect: {0}. Actual: {1}".format(ads, actual)

    def platform(self, platform):
        actual = self.driver.find_element(By.CSS_SELECTOR, 'td.col-platform').text
        if actual != platform:
            assert False, "Expect: {0}. Actual: {1}".format(platform, actual)


    def region(self, regions):
        regions = regions.split(';')
        tds = self.driver.find_elements(By.CSS_SELECTOR, 'td.col-region')
        for (region, td) in zip(regions, tds):
            actual = td.text
            if actual != region:
                assert False, "Expect: {0}. Actual: {1}".format(region, actual)


    def price(self, prices):
        prices = prices.split(';')
        tds = self.driver.find_elements(By.CSS_SELECTOR, 'td.col-price')
        for (price, td) in zip(prices, tds):
            actual = td.text
            if actual != price:
                assert False, "Expect: {0}. Actual: {1}".format(price, actual)

    

    def verify(self, **kwargs):
        dic = {

        }

        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)

