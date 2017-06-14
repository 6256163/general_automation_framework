# coding=utf-8
from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):
    # 初始化工作
    def setUp(self):
        pass

    # 退出清理工作
    def tearDown(self):
        pass

    # 初始化验证：无参数提供
    def test_1_null_command_init(self):
        runner = False
        try:
            runner = Runner()
        except TypeError:
            assert True
        else:
            assert False

    # 命令行参数验证：提供错误参数，空值。
    def test_2_invalid_command_init(self):
        runner = False
        try:
            runner = Runner([])
        except SystemExit:
            if runner:
                assert False


    # 命令行参数验证：提供错误参数，无效的参数
    def test_3_invalid_command_init(self):
        runner = False
        try:
            runner = Runner(['-t'])
        except SystemExit:
            if runner:
                assert False


    # 命令行参数验证：提供错误参数，不期望的短参数
    def test_4_invalid_command_init(self):
        runner = False
        try:
            runner = Runner(['-q', '飞机扩大解放扩大解放扩大解放棵'])
        except SystemExit:
            if runner:
                assert False


    # 命令行参数验证：提供错误参数，不期望的长参数
    def test_5_invalid_command_init(self):
        runner = False
        try:
            runner = Runner(['--q', '飞机扩大解放扩大解放扩大解放棵'])
        except SystemExit:
            if runner:
                assert False


    # 命令行参数验证：提供错误参数，短参数不全
    def test_6_invalid_command_init(self):
        runner = False
        try:
            runner = Runner(['-t', '飞机扩大解放扩大解放扩大解放棵'])
        except SystemExit:
            if runner:
                assert False


    # 命令行参数验证：提供错误参数，长参数不全
    def test_7_invalid_command_init(self):
        runner = False
        try:
            runner = Runner(['--result', '飞机扩大解放扩大解放扩大解放棵'])
        except SystemExit:
            if runner:
                assert False

    # 命令行参数验证：提供正确参数，短参数
    def test_8_invalid_command_init(self):
        runner = Runner(['-t','ttt','-r','rrr','-l','lll'])
        if runner.TC != 'ttt' or runner.LOG != 'lll' or runner.RESULT != 'rrr':
            assert False


