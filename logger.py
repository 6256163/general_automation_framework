# coding=utf-8
import os
import logging

import setting
from loader.testcase import Testcase

class Logger(object):

    def __init__(self, tc_path, time ):
        self.test_time = time
        self.tc_path = tc_path


    def get_log_file(self):
        # 创建log路径 /test_log/日期/模块名称/模块名称/用例名称.log
        log_path = os.path.join(setting.LOG_FOLDER, self.test_time, *Testcase().get_tc_module(self.tc_path))
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        tc_file = os.path.basename(self.tc_path)
        return os.path.join(log_path, tc_file + '.log')

    def setup_logging(self):

        logger = logging.getLogger("test_log")
        logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler(self.get_log_file())
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