from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url=url)

    def get_title(self):
        return self.driver.title

    def find_by(self, **kwargs):
        for by, value in kwargs.items():
            if by.upper() == "ID":
                return self.driver.find_element(by=By.ID, value=value)
            elif by.upper() == "XPATH":
                return self.driver.find_element(by=By.XPATH, value=value)
            elif by.upper() == "LINK_TEXT":
                return self.driver.find_element(by=By.LINK_TEXT, value=value)
            elif by.upper() == "PARTIAL_LINK_TEXT":
                return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=value)
            elif by.upper() == "NAME":
                return self.driver.find_element(by=By.NAME, value=value)
            elif by.upper() == "TAG_NAME":
                return self.driver.find_element(by=By.TAG_NAME, value=value)
            elif by.upper() == "CLASS_NAME":
                return self.driver.find_element(by=By.CLASS_NAME, value=value)
            elif by.upper() == "CSS_SELECTOR":
                return self.driver.find_element(by=By.CSS_SELECTOR, value=value)

