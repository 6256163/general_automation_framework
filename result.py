# coding=utf-8
import socket

from logger import Logger
from testcase import Testcase


class Result(object):
    def __init__(self, starttime):
        self.time = starttime
        self.result = {
            'time': self.time,
            'machine': socket.gethostname(),
            'modules': {}
        }

    def set_result(self, tc_path, tc_result):
        tc = Testcase()
        tc_module = tc.get_tc_module(tc_path)
        tc_name = tc.get_tc_name(tc_path)
        module_level = '.'.join(tc_module)
        if not module_level in self.result['modules'].keys():
            self.result['modules'][module_level] = {'pass': 0, 'fail': 0}
            self.result['modules'][module_level]['results'] = list()
        if tc_result:
            self.result['modules'][module_level]['pass'] += 1
        else:
            self.result['modules'][module_level]['fail'] += 1
        with open(Logger(tc_path, self.time).get_log_file(), 'r') as log:
            self.result['modules'][module_level]['results'].append(
                {'result': tc_result, 'test_case': tc_name, 'log': '<br/>'.join(log.readlines())})

    def get_result(self):
        return self.result
