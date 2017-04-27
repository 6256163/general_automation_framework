from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
import logging


class Operation(object):
    def __init__(self, driver):
        self.driver = WebDriver
        # self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info("Open page:{0}".format(url))

    def get_element(self, *loc):
        try:
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            logging.error("Fail to find element: {0} {1}".format(*loc))
            assert False, "Fail to find element: {0} {1}".format(*loc)

    def input_value(self, value, *loc):
        self.get_element(*loc).send_keys(value)
        logging.info("Input value: {0}".format(value))

    def click(self, *loc):
        self.get_element(*loc).click()
        logging.info("Click element: {0} {1}".format(*loc))

    def fetch(self, value, *loc):
        if self.driver.find_element(*loc).text == value:
            logging.info("Get string: {0}".format(value))
        else:
            assert self.driver.find_element(*loc).text == value
            logging.error("Can not find string: {0}".format(value))



