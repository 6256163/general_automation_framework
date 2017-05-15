# coding=utf-8
import codecs
import os
import re

import setting


class Testcase(object):
    def __init__(self):
        self.folder = setting.TESTCASE_FOLDER

    def get_csv_list(self, dir=None, file_list=list()):
        """
        :param dir: testcase folder path
        :param file_list: return value for recursion
        :return: list for csv paths
        """
        if dir == None:
            dir = self.folder
        if os.path.isfile(dir):
            file_list.append((dir))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                self.get_csv_list(newDir, file_list)
        return sorted(file_list)

    def get_line(self, path):
        csv_datas = list()
        # 读取当前csv
        with codecs.open(path, 'r', 'utf-8') as testcase:
            for line in testcase.readlines():
                csv_datas.append(line.strip('\n').strip('\r').split(','))
        return csv_datas[1:]

    def get_steps(self, path):
        """
        :param path: csv file path
        :return: A dicts list for testcase steps [{},{},{}...]
        """
        csv_datas = list()
        steps = list()
        with codecs.open(path, 'r', 'utf-8') as testcase:
            for line in testcase.readlines():
                csv_datas.append(line.strip('\n').strip('\r').split(','))
        for i, data in enumerate(csv_datas):
            if i > 0:
                steps.append(dict(zip(csv_datas[0], data)))
        return steps

    pattern = re.compile(setting.TESTCASE_FOLDER + "(.*?)" + ".csv")

    def get_tc_module(self, path):
        module = self.pattern.search(path).groups()[0].split(os.sep)[1:-1]
        if module == []:
            module.append('Null')

    def get_tc_name(self, path):
        return os.path.basename(path)


