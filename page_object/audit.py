# coding=utf-8
from __future__ import absolute_import

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class Audit(BasePage):
    def __init__(self, driver):
        super(Audit, self).__init__(driver)


    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


    def get_audit_num(self, **kwargs):

        xpath = '//p[contains(text(),"{0}")]/' \
                '../dl//dt[contains(text(),"{1}")]/following-sibling::dd[1]/a'.format(kwargs['阶段'],kwargs['状态'])

        return self.get_element(By.XPATH,xpath).text
