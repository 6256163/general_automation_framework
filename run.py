#!/usr/bin/env Python
# coding=utf-8
import codecs
import os
import socket
import time

from jinja2 import Environment, PackageLoader
import setting
from test import Test


class Run():
    def __init__(self):
        self.result = {
            'time': time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())),
            'machine': socket.gethostname(),
            'modules': {}
        }

    def run(self):
        file_list = self.GetFileList(setting.TESTCASE_FOLDER, [])
        file_list.sort()
        for f in file_list:
            test = Test(f, self.result['time'])
            r = test.execute_tc()

            if not '.'.join(f[1]) in self.result['modules'].keys():
                self.result['modules']['.'.join(f[1])] = {'pass': 0, 'fail': 0}
                self.result['modules']['.'.join(f[1])]['results'] = list()
            if r:
                self.result['modules']['.'.join(f[1])]['pass'] += 1
            else:

                self.result['modules']['.'.join(f[1])]['fail'] += 1
            with open(test.log_file,'r') as log:
                self.result['modules']['.'.join(f[1])]['results'].append({'result': r, 'test_case': f[2], 'log':'<br/>'.join(log.readlines())})
            # self.result['results'].append(results)

        env = Environment(loader=PackageLoader("template_package", 'templates'))
        template = env.get_template('template.html')

        if not os.path.exists(setting.TEST_RESULTS_FOLDER):
            os.makedirs(setting.TEST_RESULTS_FOLDER)

        #创建result文件
        result_html= setting.TEST_RESULTS_FOLDER + os.sep + self.result['time'] + '.html'
        with codecs.open(result_html, 'w', 'utf-8') as res:
            res.write(template.render(result=self.result))

    def GetFileList(self, dir, fileList):
        if os.path.isfile(dir):
            # 获取模块信息module_level
            import re
            pattern = re.compile(setting.TESTCASE_FOLDER + "(.*?)" + ".csv")
            module = pattern.search(dir).groups()
            module_level = module[0].split(os.sep)
            del module_level[0]

            testcase = module_level.pop()
            if module_level ==[]:
                module_level = ['null']
            fileList.append((dir, module_level, testcase))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                self.GetFileList(newDir, fileList)
        return sorted(fileList)


if __name__ == '__main__':
    run = Run()
    run.run()
