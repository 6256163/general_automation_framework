import os
import platform
import unittest

import setting
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
            chromedriver = path + "\\browser_driver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        cls.chrome_driver = WebDriver(chromedriver)
        cls.chrome_driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.chrome_driver.quit()
        super(TestRun, cls).tearDownClass()


    def test(self):
        file_list = self.GetFileList(setting.TESTCASE_FOLDER, [])
        for f in file_list:
            test = Test(self.chrome_driver,f)
            test.execute_tc(os.path.join(os.getcwd(), f))

    def GetFileList(self, dir, fileList):
        if os.path.isfile(dir):
            fileList.append(dir.decode('gbk'))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                self.GetFileList(newDir, fileList)
        return fileList.sort()


if __name__ == '__main__':
    testresult = TestRun('test')