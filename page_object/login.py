from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.base_page import BasePage


class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self.open_page('http://wx-pre-t.quantone.com/web/index.php?c=user&a=login&p=quantoneadminlogin')

    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.NAME, 'submit')


    def login_form(self, **kwargs):
        # input username
        if kwargs.get('username', ''):
            self.input(kwargs['username'], *self.USERNAME)
        else:
            assert False, "Username don't set"

        # input
        if kwargs.get('password', ''):
            self.input(kwargs['password'], *self.PASSWORD)
        else:
            assert False, "Password don't set"

        self.click(*self.SUBMIT)
        sleep(5)



