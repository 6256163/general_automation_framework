# coding=utf-8
from __future__ import absolute_import

from time import sleep

import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage


class Stock(BasePage):
    def __init__(self, driver):
        super(Stock, self).__init__(driver)


    map = {
        'price_process':'sys_customersBap'
    }


    def modufy_flow(self, process):

        self.input('')

