from selenium.webdriver.chrome.webdriver import WebDriver

from executer.operation import Operation


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.ope = Operation(driver=driver)

    def perform(self, func, **kwargs):
        self.__getattribute__(func)(**kwargs)

    def open_page(self, url):
        self.driver.get(url=url)

    def get_title(self):
        return self.driver.title

    def get_element(self, *args):
        return self.ope.get_element(*args)

    def get_elements(self, *args):
        return self.ope.get_elements(*args)

    def click(self, *args):
        self.get_element(*args).click()

    def input(self, input, *args):
        target = self.get_element(*args)
        target.clear()
        target.send_keys(input)