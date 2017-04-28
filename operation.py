from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
import logging


class Operation(object):
    def __init__(self, driver):
        #self.driver = WebDriver
        self.driver = driver

####################### For Test Action################
    def open_page(self, url_):
        self.driver.get(url_)
        self.driver.maximize_window()
        logging.info("Open page:{0}".format(url_))

    def input_value(self, value, *loc):
        self.get_element(*loc).send_keys(value)
        logging.info("Input value: {0}".format(value))

    def click(self, *loc):
        self.get_element(*loc).click()
        logging.info("Click element: {0} {1}".format(*loc))



####################### For Expected Result Validation################
    def verify(self, value, property, *loc):
        actual_result = None

        if property.upper() == "TEXT":
            actual_result = self.get_element(*loc).text
        elif property.upper() == "":
            pass

        else:
            raise Exception

        if actual_result == value:
            logging.info("Get string: {0}".format(value))
        else:
            assert False, logging.error("Get wrong value:{0}. Expected:{1}".format(actual_result, value))

    def compare(self,):
        pass


####################### For Public Function################
    def get_element(self, *loc):
        try:
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            assert False, "Fail to find element: {0} {1}".format(*loc)