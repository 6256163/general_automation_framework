import os
from unittest import TestCase
from testcase import Testcase


class TestcaseTest(TestCase):
    # 初始化工作
    def setUp(self):
        self.tc = Testcase(tc_folder='')

    # 退出清理工作
    def tearDown(self):
        pass

    # csv文件路径获取验证
    def test_1_get_csv_files(self):
        path = os.path.join('tests','test_data_folder')
        file_list = self.tc.get_csv_list(path)



    # csv读取验证
    def test_1_read_csv_lines(self):
        tc = Testcase(tc_folder='')
        tc.get_line()