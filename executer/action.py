# coding=utf-8
import os
from time import sleep

from .operation import Operation


class Action(Operation):

    def __init__(self, csv):
        super(Action,self).__init__(csv)

    def open_page(self):
        # 直接用href地址打开网页
        if not self.csv['ActionLocation']:
            self.driver.get(self.csv['ActionValue'])
        # ActionLocation 表示HTML存放路径， ActionValue 表示HTML文件名
        else:
            href = r'file://' + os.path.join(os.getcwd(), self.csv['ActionLocation'], self.csv['ActionValue'])
            self.driver.get(href)

    def input_value(self):
        target = self.get_element(self.csv['ActionBy'], self.csv['ActionLocation'])
        target.clear()
        target.send_keys(self.csv['ActionValue'])

    def click(self):
        sleep(3)
        self.get_element(self.csv['ActionBy'], self.csv['ActionLocation']).click()

    def switch_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            if self.driver.title == self.csv['ActionValue']:
                break

    def open_new_page(self):
        if self.csv['ActionBy'] and self.csv['ActionLocation']:
            href = self.get_element(self.csv['ActionBy'], self.csv['ActionLocation']).get_attribute('href')
        else:
            href = self.csv['ActionValue']
        js = 'window.open("{0}");'.format(href)
        self.driver.execute_script(js)


    def switch_frame(self):
        if self.csv['ActionBy'] == '':
            self.driver.switch_to.frame(self.csv['ActionLocation'])
        else:
            self.driver.switch_to.frame(self.get_element(self.csv['ActionBy'],self.csv['ActionLocation']))

    def switch_default_content(self):
        self.driver.switch_to.default_content()

    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()
