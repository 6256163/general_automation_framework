# coding=utf-8
import logging

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from analysis import Analysis


class Operation(object):

    def __init__(self, driver):
        # self.driver = WebDriver
        self.driver = driver

    ####################### For Test Action################
    def open_page(self, url_):
        self.driver.get(url_)
        # self.driver.maximize_window()
        #logging.info("Open page:{0}".format(url_))

    def input_value(self, value, loc):
        self.get_element(loc).clear()
        self.get_element(loc).send_keys(value)
        #logging.info("Input value: {0}".format(value))

    def click(self, loc):
        self.get_element(loc).click()
        #logging.info("Click element: {0} {1}".format(loc['by'], loc['value']))

    def switch_window(self, title):
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            if self.driver.title == title:
                break


    def open_new_page(self, href):
        if isinstance(href, dict):
            href = self.get_element(href).get_attribute('href')
        js = 'window.open("{0}");'.format(href)
        self.driver.execute_script(js)

    ####################### For Expected Result Validation################
    def verify(self, value, property, loc):
        actual_result = self.get_property_value(property, loc)

        if actual_result != value:
            assert False, u"Get wrong value:{0}. Expected:{1}".format(actual_result, value)

    def compare(self, bys, locations, properties):
        analysis = Analysis()
        values = list()
        time.sleep(3)
        for by, location, property in zip(bys, locations, properties):
            loc = analysis.get_loc(by, location)
            value = self.get_property_value(property,loc)
            values.append(value)
        for i in range(len(values)):
            if values[0].lower() == values[i].lower():
                pass
            else:
                assert False, u"Compreation {0} are not equal".format(values)


    ####################### For Public Function################
    def get_element(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(**loc).is_displayed())
            return self.driver.find_element(**loc)
        except NoSuchElementException(msg=u"Fail to find element: {0} {1}".format(loc['by'], loc['value'])):
            assert False, u"Fail to find element: {0} {1}".format(loc['by'], loc['value'])


    def get_property_value(self,property, loc):
        if property.upper() == "TEXT":
            return self.get_element(loc).text
        else:
            return self.get_element(loc).get_attribute(property)

