# coding=utf-8
import os
import platform

from selenium import webdriver

import setting
from .action import Action
from .expect import Expect


class Execution(Action, Expect):
    def __init__(self, csv):
        super(Execution, self).__init__(csv)
        self.setup_driver()

    def execute(self):

        execut = getattr(Execution, self.csv['Action'].lower())
        execut()
        # if self.csv['Action'].upper() in [
        #     'INPUT_VALUE',
        #     'OPEN_PAGE',
        #     'CLICK',
        #     'SWITCH_WINDOW',
        #     'OPEN_NEW_PAGE',
        # ]:
        #     execut = getattr(Execution, self.csv['Action'].lower())
        #     execut()
        #
        # if self.csv['Expect'].upper() in [
        #     "VERIFY",
        #     "COMPARE"
        # ]:
        #     execut = getattr(Execution, self.csv['Expect'].lower())
        #     execut()

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
