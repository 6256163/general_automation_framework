# coding=utf-8
import socket

from logger import Logger
from testcase import Testcase


class Result(object):
    def __init__(self, starttime, result_folder):
        """
        :param starttime: test start time
        :param result_folder: test result folder
        """
        self.time = starttime
        self.result_folder=result_folder
        self.result = {
            'time': self.time,
            'machine': socket.gethostname(),
            'modules': {}
        }

    def set_result(self, tc_result, tc_name, tc_module, log_file):
        """
        :param tc_result: execution result
        :param tc_name: tc file name
        :param tc_module: tc folder name as module name
        :param log_file: log file path
        :return: 
        """
        module_level = '.'.join(tc_module)
        if not module_level in self.result['modules'].keys():
            self.result['modules'][module_level] = {'pass': 0, 'fail': 0}
            self.result['modules'][module_level]['results'] = list()
        if tc_result:
            self.result['modules'][module_level]['pass'] += 1
        else:
            self.result['modules'][module_level]['fail'] += 1
        with open(log_file, 'r') as log:
            self.result['modules'][module_level]['results'].append(
                {'result': tc_result, 'test_case': tc_name, 'log': '<br/>'.join(log.readlines())})

    def get_result(self):
        return self.result
