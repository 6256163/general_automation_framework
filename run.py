import os
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver

from test import Test

class TestRun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestRun, cls).setUpClass()
        path = os.getcwd()
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
        test.execute_tc(r"D:\study\general_automation_framework\testcase.csv")


if __name__ == '__main__':
    testresult = TestRun('test_1')