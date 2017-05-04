import os
import logging

import time

import setting
from operation import Operation
from analysis import Analysis
import codecs



class Test(object):
    frame_driver = None
    frame_flag = 0

    def __init__(self, driver,testcase_path):
        self.driver = driver
        tc = testcase_path.split(setting.TESTCASE_FOLDER)[1]
        log_file = os.path.join(setting.LOG_FOLDER, tc + '.log')
        log_folder = os.path.pardir(log_file)
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        logging.basicConfig(filename=log_file, level=logging.INFO)


    def execute_tc(self, path):
        csv_datas = list()
        with codecs.open(path,'r','utf-8') as testcase:
            for line in testcase.readlines():
                csv_datas.append(line.strip('\n').split(','))
        logging.info("==========start testcase {}===========".format(csv_datas[0][0]))
        for i, data in enumerate(csv_datas):
            if i > 0:
                tc_data = dict(zip(csv_datas[0], data))
                if tc_data['Action']:
                    self.execute_action(tc_data)
                if tc_data['Expect']:
                    self.verify_expect(tc_data)
        logging.info("==========finish testcase {}===========".format(csv_datas[0][0]))


    def execute_action(self, datas):
        operation = Operation(self.driver)
        analysis = Analysis()
        loc = analysis.get_loc(datas['ActionBy'],datas['ActionLocation'])

        if datas['Action'].upper() == "INPUT_VALUE":
            operation.input_value(datas['ActionValue'], loc)
        elif datas['Action'].upper() == "OPEN_PAGE":
            if datas['ActionLocation'] == '':
                operation.open_page(datas['ActionValue'])
            else:
                path = os.path.join(os.getcwd(),datas['ActionLocation'],datas['ActionValue'])
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
            operation.compare(datas['ExpectBy'].split(';'),datas['ExpectLocation'].split(';'), datas['ExpectProperty'].split(';'))
        else:
            pass

