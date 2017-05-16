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
            logger = Logger(f, self.time).setup_logging()
            steps = tc.get_steps(f)
            csv_lines = tc.get_line(f)
            #result init
            r = True
            exe = Execution(steps[0])
            for step, line in (zip(steps, csv_lines)):
                try:
                    logger.info(str(line))
                    exe.update_step(step)
                    exe.execute()
                except Exception as e:
                    r = False
                    logger.exception(e)
                    break
            exe.quit()
            tc_result.set_result(f, r)
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
