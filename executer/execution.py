# coding=utf-8
from __future__ import absolute_import

import os
import platform

from selenium import webdriver
from page_object.page_object import PageObject
import setting
from .action import Action
from .expect import Expect


class Execution(Action, Expect):
    def __init__(self, csv):
        super(Execution, self).__init__(csv)
        self.setup_driver()
        self.driver.maximize_window()

    def update_step(self, step):
        self.csv = step

    def execute(self):
        if self.csv['PageObject']:
            kwarg = dict()
            if self.csv['PageValue']:
                for item in self.csv['PageValue'].split('|'):
                    kwarg[item.split('=')[0]] = item.split('=')[1]
            po = PageObject().get_instence(self.csv['PageObject'])(self.driver).perform(self.csv['PageAction'], **kwarg)
        if self.csv['Action']:
            getattr(Execution, self.csv['Action'].lower())(self)
        if self.csv['Expect']:
            getattr(Execution, self.csv['Expect'].lower())(self)

    def setup_driver(self):
        if self.driver is None:
            if platform.platform().startswith("Win"):
                suffix = '.exe'
            else:
                suffix = ''
            if self.csv['Browser'].upper() == "CHROME":
                driver_path = os.path.join(setting.BROWSER_DRIVER_FOLDER, 'chromedriver' + suffix)
                os.environ["webdriver.chrome.driver"] = driver_path
                self.driver = webdriver.Chrome(driver_path)

            # 添加其他webdriver
            elif self.csv['Browser'].upper() == "FIREFOX":
                pass

            self.driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()