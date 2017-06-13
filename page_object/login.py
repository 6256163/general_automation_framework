# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By
from base_page import BasePage


class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self.open_page('http://weimaxpre.cnsuning.com/web/index.php?c=user&a=login&p=quantoneadminlogin')

    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.NAME, 'submit')

    # 用户登录
    def login(self, **kwargs):
        # input username
        if kwargs.get('username', ''):
            self.input(kwargs['username'], *self.USERNAME)
        else:
            assert False, "Username don't set"

        # input password
        if kwargs.get('password', ''):
            self.input(kwargs['password'], *self.PASSWORD)
        else:
            assert False, "Password don't set"
        # 提交
        self.click(*self.SUBMIT)
        sleep(5)



