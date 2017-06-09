# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Operation(object):
    def __init__(self, csv = None, driver = None):
        self.driver = driver
        self.csv = csv

    def get_element(self, by, value):
        """
        :param by: By.ID,By.name,By.link_text ...
        :param value: value for By.ID,By.name,By.link_text ...
        :return: WebElement object
        """
        loc = self.get_loc(by, value)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(**loc).is_displayed())
            return self.driver.find_element(**loc)
        except NoSuchElementException(msg=u"Fail to find element: {0} {1}".format(loc['by'], loc['value'])):
            assert False, u"Fail to find element: {0} {1}".format(loc['by'], loc['value'])

    def get_elements(self, by, value):
        """
        :param by: By.ID,By.name,By.link_text ...
        :param value: value for By.ID,By.name,By.link_text ...
        :return: WebElement object
        """
        loc = self.get_loc(by, value)
        return self.driver.find_elements(**loc)


    def get_property_value(self, by, value, property):
        """
        :param by: By.ID,By.name,By.link_text ...
        :param value: value for By.ID,By.name,By.link_text ...
        :param property: dom property
        :return: dom property value
        """
        if property.upper() == "TEXT":
            return self.get_element(by, value).text
        else:
            return self.get_element(by, value).get_attribute(property)

    def get_loc(self, by, value):
        """
        :param by: By.ID,By.name,By.link_text ...
        :param value: value for By.ID,By.name,By.link_text ...
        :return: dict {by=, value=,}
        """
        if by.upper() == "XPATH":
            return {'by': By.XPATH, 'value': value}
        elif by.upper() == "ID":
            return {'by': By.ID, 'value': value}
        elif by.upper() in ["CSS_SELECTOR", "CSS SELECTOR"]:
            return {'by': By.CSS_SELECTOR, 'value': value}
        elif by.upper() in ["TAG_NAME", "TAG NAME"]:
            return {'by': By.TAG_NAME, 'value': value}
        elif by.upper() in ["LINK_TEXT", "LINK TEXT"] :
            return {'by': By.LINK_TEXT, 'value': value}
        elif by.upper() == "NAME":
            return {'by': By.NAME, 'value': value}
        elif by.upper() in ["CLASS_NAME", "CLASS NAME"]:
            return {'by': By.CLASS_NAME, 'value': value}
        elif by.upper() in ["PARTIAL_LINK_TEXT","PARTIAL LINK TEXT"]:
            return {'by': By.PARTIAL_LINK_TEXT, 'value': value}
        else:
            pass

    def get_compare(self, expectBy, expectLocation):
        """
        :param list of by, splited by ';'
        :param value list of by, splited by ';'
        :return: list of dict {by=, value=,}
        """
        bys = expectBy.split(';')
        locs = expectLocation.split(';')
        return [self.get_loc(bys[0], locs[0]), self.get_loc(bys[1], locs[1])]
