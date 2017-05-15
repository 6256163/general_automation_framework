# coding=utf-8
import codecs
import os
import time

import setting
from jinja2 import Environment, PackageLoader
from result import Result

from executer.execution import Execution
from logger import Logger
from testcase import Testcase


class Runner(object):
    def __init__(self):
        self.time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    def run(self):
        tc = Testcase()
        file_list = tc.get_csv_list()
        r = True
        tc_result = Result(self.time)
        for f in file_list:
            logger = Logger(f,self.time).setup_logging()
            r = True
            for step, csv_line in (zip(tc.get_steps(f), tc.get_line(f))):
                try:
                    exe = Execution(step)
                    logger.info(csv_line)
                    exe.execute()
                except Exception as e:
                    r = False
                    logger.exception(e)
                    break
            tc_result.set_result(f,r)
        env = Environment(loader=PackageLoader("template_package", 'templates'))
        template = env.get_template('template.html')

        if not os.path.exists(setting.TEST_RESULTS_FOLDER):
            os.makedirs(setting.TEST_RESULTS_FOLDER)

        # 创建result文件
        result_html = setting.TEST_RESULTS_FOLDER + os.sep + tc_result.get_result()['time'] + '.html'
        with codecs.open(result_html, 'w', 'utf-8') as res:
            res.write(template.render(result=tc_result.get_result()))


if __name__ == "__main__":
    run = Runner()
    run.run()