import os
import platform
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver


from test import Test

class TestRun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestRun, cls).setUpClass()
        path = os.getcwd()
        if platform.platform().startswith("Darwin"):
            chromedriver = path + "/browser_driver/chromedriver"
        else:
            chromedriver = path + "/browser_driver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        cls.chrome_driver = WebDriver(chromedriver)
        cls.chrome_driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.chrome_driver.quit()
        super(TestRun, cls).tearDownClass()


    def test_1(self):
        test = Test(self.chrome_driver)
        testcase = r'testcase.csv'
        if platform.platform().startswith("Darwin"):
            folder = r"/"
        else:
            folder = '\\'
        test.execute_tc(os.getcwd() + folder+testcase)


if __name__ == '__main__':
    testresult = TestRun('test_1')