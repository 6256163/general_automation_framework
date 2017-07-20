# coding=utf-8
import codecs
import os
import time
import sys, getopt
import setting
from jinja2 import Environment, PackageLoader
from result import Result

from executer.execution import Execution
from logger import Logger
from testcase import Testcase


class Runner(object):
    def __init__(self, command_line):
        self.command_line = command_line
        self.time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        self.TC = setting.TESTCASE_FOLDER
        self.RESULT = setting.TEST_RESULTS_FOLDER
        self.LOG = setting.LOG_FOLDER
        # self.process_command_line()

    def run(self):

        tc = Testcase(self.TC)
        file_list = tc.get_csv_list()
        r = True
        tc_result = Result(self.time, self.RESULT)
        # 循环执行 CSV 文件
        for f in file_list:
            # 初始化 logger
            my_log = Logger(f, self.time, self.LOG)
            logger = my_log.setup_logging()
            # 获取csv步骤，数据与关键字拼装
            steps = tc.get_steps(f)
            # 逐行读取csv
            csv_lines = tc.get_line(f)
            # result init
            r = True
            exe = Execution(steps[0])
            for step, line in (zip(steps, csv_lines)):
                try:
                    logger.info(str(line))
                    exe.update_step(step)
                    log=exe.execute()
                    if log:
                        r = False
                        logger.info(log)
                except Exception as e:
                    r = False
                    logger.exception(e)
                    break
            exe.quit()
            tc_result.set_result(r, tc.get_tc_name(f), tc.get_tc_module(f), my_log.get_log_file())
        env = Environment(loader=PackageLoader("template_package", 'templates'))
        template = env.get_template('template.html')

        # 创建result文件
        result_html = self.RESULT + os.sep + tc_result.get_result()['time'] + '.html'
        with codecs.open(result_html, 'w', 'utf-8') as res:
            res.write(template.render(result=tc_result.get_result()))

    def process_command_line(self):
        # 命令行参数处理
        try:
            if not self.command_line:
                raise getopt.GetoptError('')
            opts, args = getopt.getopt(self.command_line, "t:r:l:", ["testcase=", "result=", "log="])
        except getopt.GetoptError:
            print('runner.py -t <testcase path> -r <result path> -l <log path>')
            sys.exit()
        for opt, arg in opts:
            if opt in ("-t", "--testcase"):
                self.TC = arg
            elif opt in ("-r", "--result"):
                self.RESULT = arg
            elif opt in ("-l", "--log"):
                self.LOG = arg
        if self.RESULT == None or self.LOG == None or self.TC == None:
            sys.exit()


if __name__ == "__main__":
    run = Runner(sys.argv[1:])
    run.run()
