# coding=utf-8
import os

from .action import Action
from .expect import Expect


class Execution(Action, Expect):
    def __init__(self, driver, csv):
        super(Execution, self).__init__(driver, csv)

    def execute(self):

        if self.csv['Action'].upper() in [
            'INPUT_VALUE',
            'OPEN_PAGE',
            'CLICK',
            'SWITCH_WINDOW',
            'OPEN_NEW_PAGE',
        ]:
            execut = getattr(Execution, self.csv['Action'].lower())
            execut()

        if self.csv['Expect'].upper() in [
            "VERIFY",
            "COMPARE"
        ]:
            execut = getattr(Execution, self.csv['Expect'].lower())
            execut()

            # if self.csv['Action'].upper() == "INPUT_VALUE":
            #     self.input_value()
            #
            # elif self.csv['Action'].upper() == "OPEN_PAGE":
            #     self.open_page()
            #
            # elif self.csv['Action'].upper() == "CLICK":
            #     self.click()
            #
            # elif self.csv['Action'].upper() == "SWITCH_WINDOW":
            #     self.switch_window()
            #
            # elif self.csv['Action'].upper() == "OPEN_NEW_PAGE":
            #     self.open_new_page()
            #
            # elif self.csv['Action'].upper() == "SWITCH_FRAME":
            #     # 通过ID或name属性值切换frame
            #     if self.csv['ActionBy'] == '':
            #         self.driver.switch_to.frame(self.csv['ActionLocation'])
            #     # 通过WebElement切换frame
            #     else:
            #         self.driver.switch_to.frame(self.get_element(self.csv['ActionBy'], self.csv['ActionLocation']))
            #
            # elif self.csv['Action'].upper() == "SWITCH_DEFAULT_CONTENT":
            #     self.driver.switch_to.default_content()
            #
            # elif self.csv['Action'].upper() == "SWITCH_PARENT_FRAME":
            #     self.driver.switch_to.parent_frame()

        if self.csv['Expect']:

            if self.csv['Expect'].upper() == "VERIFY":
                self.verify()
            elif self.csv['Expect'].upper() == "COMPARE":
                self.compare()
