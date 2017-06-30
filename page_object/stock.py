# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage


class Stock(BasePage):
    # 选取投放日期
    def select_date(self, date_from, date_to):
        """
        :param date_from: 起始日期
        :param date_to: 截至日期
        :return: 
        """
        # 点击日期选择器
        filter_date_picker = self.get_element(By.ID, 'filterDatepicker')
        filter_date_picker.click()
        # 输入起止时间
        self.input(date_from, *(By.CSS_SELECTOR, 'input.start',))
        self.input(date_to, *(By.CSS_SELECTOR, 'input.end',))
        # 点击确定
        self.click(By.CSS_SELECTOR, 'button.enter')



        selecters = self.get_elements(By.CLASS_NAME, 'adr')
        ad_selector = selecters[0].find_element(By.XPATH, '../button')
        area_selector = selecters[1].find_element(By.XPATH, '../button')
        content_selector = selecters[2].find_element(By.XPATH, '../button')
        tracker_selector = selecters[3].find_element(By.XPATH, '../button')
