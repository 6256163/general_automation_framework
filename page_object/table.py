# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By

from .base_page import BasePage

class Table(BasePage):
    def __init__(self, driver):
        super(Table, self).__init__(driver)

