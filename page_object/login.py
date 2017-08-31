# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base_page import BasePage



class Login(BasePage):
    def __init__(self, driver, url = 'http://10.200.44.43/site/superentrance'):
        super(Login, self).__init__(driver)
        self.url = url

    USERNAME = (By.ID, 'LoginForm_username')
    PASSWORD = (By.ID, 'LoginForm_password')
    VERIFYCODE = (By.ID, 'LoginForm_verifyCode')
    SUBMIT = (By.ID, 'login')

    # 用户登录
    def login(self, **kwargs):
        self.open_page(self.url)
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

        if kwargs.get('verifycode', ''):
            self.input(kwargs['verifycode'], *self.VERIFYCODE)
        else:
            assert False, "Password don't set"

        # 提交
        self.click(*self.SUBMIT)
        self.wait_ajax_loading()

    def logout(self):
        self.click(By.ID,'logout')
        sleep(2)
