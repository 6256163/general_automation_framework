#!/usr/bin/env Python
# coding=utf-8
import os
import time
import shutil

from jinja2 import Environment, PackageLoader
import setting
from test import Test


class Run():
    def __init__(self):
        self.result = dict()

    def run(self):
        self.achieve_log()
        file_list = self.GetFileList(setting.TESTCASE_FOLDER, [])
        file_list.sort()
        self.result['time'] = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        import socket
        self.result['machine'] = socket.gethostname()
        self.result['results'] = list()
        for f in file_list:
            test = Test(f[0])
            results = dict()
            results[f[0]] = {'module': f[1], 'test_case': f[2]}
            results[f[0]]['result'] = test.execute_tc()
            self.result['results'].append(results)

        env = Environment(loader=PackageLoader(os.getcwd(), 'templates'))
        template = env.get_template('template.html')

        if not os.path.exists(setting.TEST_RESULTS_FOLDER):
            os.makedirs(setting.TEST_RESULTS_FOLDER)
        with open(setting.TEST_RESULTS_FOLDER + os.sep + self.result['time'] + '.html') as res:
            res.write(template.render(results=self.result))

    def GetFileList(self, dir, fileList):
        if os.path.isfile(dir):
            # 获取模块信息module_level
            import re
            pattern = re.compile(setting.TESTCASE_FOLDER + "(.*?)" + ".csv")
            module = pattern.search(dir).groups()
            module_level = module[0].split(os.sep)
            del module_level[0]
            testcase = module_level.pop()
            fileList.append((dir, module_level, testcase))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                self.GetFileList(newDir, fileList)
        return sorted(fileList)

    def achieve_log(self):
        # 归档历史log
        if os.path.exists(setting.LOG_FOLDER):
            achieve_folder = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
            achieve_path = os.path.join(setting.LOG_FOLDER, achieve_folder)
            os.makedirs(achieve_path)
            for s in os.listdir(setting.LOG_FOLDER):
                if s.split('.')[-1].upper() == "LOG":
                    shutil.move(os.path.join(setting.LOG_FOLDER, s), achieve_path)


if __name__ == '__main__':
    run = Run()
    run.run()
