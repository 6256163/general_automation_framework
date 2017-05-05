#!/usr/bin/env Python
# coding=utf-8
import os
import logging
import platform
import codecs

from selenium import webdriver

import setting
from operation import Operation
from analysis import Analysis


class Test(object):
    frame_driver = None
    frame_flag = 0

    def __init__(self, testcase_path):
        self.driver = None
        self.tc = testcase_path


    def execute_tc(self):
        logger = self.setup_logging(self.tc)
        csv_datas = list()
        # 读取当前csv
        with codecs.open(self.tc, 'r', 'utf-8') as testcase:
            for line in testcase.readlines():
                csv_datas.append(line.strip('\n').strip('\r').split(','))
        logger.info("==========start testcase {}===========".format(csv_datas[1][0]))
        # 按csv行执行testcase
        for i, data in enumerate(csv_datas):
            try:
                if i > 0:
                    tc_data = dict(zip(csv_datas[0], data))
                    # 设置WebDriver
                    if self.driver == None:
                        self.setup_driver(tc_data['Browser'])

                    # 执行Action
                    if tc_data['Action']:
                        self.execute_action(tc_data)

                    # 执行Expect
                    if tc_data['Expect']:
                        self.verify_expect(tc_data)

                    logging.info(csv_datas[i])
            except Exception as e:
                logger.error(e)
                break
        self.driver.quit()
        logger.info("==========finish testcase {}===========".format(csv_datas[1][0]))


    def execute_action(self, datas):
        operation = Operation(self.driver)
        analysis = Analysis()
        loc = analysis.get_loc(datas['ActionBy'], datas['ActionLocation'])

        if datas['Action'].upper() == "INPUT_VALUE":
            operation.input_value(datas['ActionValue'], loc)
        elif datas['Action'].upper() == "OPEN_PAGE":
            if datas['ActionLocation'] == '':
                operation.open_page(datas['ActionValue'])
            else:
                path = os.path.join(os.getcwd(), datas['ActionLocation'], datas['ActionValue'])
                operation.open_page(path)
        elif datas['Action'].upper() == "CLICK":
            operation.click(loc)
        elif datas['Action'].upper() == "SWITCH_FRAME":
            if datas['ActionBy'] == '':
                self.driver.switch_to.frame(datas['ActionLocation'])
            else:
                self.driver.switch_to.frame(operation.get_element(loc))
        elif datas['Action'].upper() == "SWITCH_DEFAULT_CONTENT":
            self.driver.switch_to.default_content()
        elif datas['Action'].upper() == "SWITCH_PARENT_FRAME":
            self.driver.switch_to.parent_frame()
        elif datas['Action'].upper() == "SWITCH_WINDOW":
            operation.switch_window(datas['ActionValue'])
        elif datas['Action'].upper() == "OPEN_NEW_PAGE":
            if datas['ActionValue'] != '':
                loc = datas['ActionValue']
            operation.open_new_page(loc)
        else:
            pass


    def verify_expect(self, datas):
        operation = Operation(self.driver)
        analysis = Analysis()
        loc = analysis.get_loc(datas['ExpectBy'], datas['ExpectLocation'])

        if datas['Expect'].upper() == "VERIFY":
            operation.verify(datas['ExpectValue'], datas['ExpectProperty'], loc)
        elif datas['Expect'].upper() == "COMPARE":
            operation.compare(datas['ExpectBy'].split(';'), datas['ExpectLocation'].split(';'),
                              datas['ExpectProperty'].split(';'))
        else:
            pass


    def setup_driver(self, driver_name):
        if platform.platform().startswith("Win"):
            suffix = '.exe'
        else:
            suffix = ''
        if driver_name.upper() == "CHROME":
            driver_path = os.path.join(setting.BROWSER_DRIVER_FOLDER, 'chromedriver' + suffix)
            os.environ["webdriver.chrome.driver"] = driver_path
            self.driver = webdriver.Chrome(driver_path)

        # 添加其他webdriver
        elif driver_name.upper() == "FIREFOX":
            pass

        self.driver.implicitly_wait(10)



    def setup_logging(self, testcase_path):
        tc_file = os.path.basename(testcase_path)
        log_file = os.path.join(setting.LOG_FOLDER, tc_file + '.log')
        if not os.path.exists(setting.LOG_FOLDER):
            os.makedirs(setting.LOG_FOLDER)

        logger = logging.getLogger("test_log")
        logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        if len(logger.handlers) == 0:
            logger.addHandler(handler)
        else:
            logger.handlers[0] = handler
        return logger



