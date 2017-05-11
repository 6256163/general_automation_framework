# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Operation(object):
    def __init__(self, driver, csv):
        self.driver = driver
        self.csv = csv

    def get_element(self, by, value):
        loc = self.get_loc(by, value)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(**loc).is_displayed())
            return self.driver.find_element(**loc)
        except NoSuchElementException(msg=u"Fail to find element: {0} {1}".format(loc['by'], loc['value'])):
            assert False, u"Fail to find element: {0} {1}".format(loc['by'], loc['value'])

    def get_property_value(self, by, value, property):
        if property.upper() == "TEXT":
            return self.get_element(by, value).text
        else:
            return self.get_element(by, value).get_attribute(property)

    def get_loc(self, by, value):
        if by.upper() == "XPATH":
            return {'by': By.XPATH, 'value': value}
        elif by.upper() == "ID":
            return {'by': By.ID, 'value': value}
        elif by.upper() == "CSS_SELECTOR":
            return {'by': By.CSS_SELECTOR, 'value': value}
        elif by.upper() == "TAG_NAME":
            return {'by': By.TAG_NAME, 'value': value}
        elif by.upper() == "LINK_TEXT":
            return {'by': By.LINK_TEXT, 'value': value}
        elif by.upper() == "NAME":
            return {'by': By.NAME, 'value': value}
        elif by.upper() == "CLASS_NAME":
            return {'by': By.CLASS_NAME, 'value': value}
        elif by.upper() == "PARTIAL_LINK_TEXT":
            return {'by': By.PARTIAL_LINK_TEXT, 'value': value}
        else:
            pass

    def get_compare(self, expectBy, expectLocation):
        bys = expectBy.split(';')
        locs = expectLocation.split(';')
        return [self.get_loc(bys[0], locs[0]), self.get_loc(bys[1], locs[1])]
