# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.base_page import BasePage


class Console(BasePage):
    def __init__(self, driver):
        super(Console, self).__init__(driver)

    # 通用元素定位信息
    add_new_user = (By.LINK_TEXT, '+添加新用户')
    add_new_group = (By.LINK_TEXT, '添加组织架构')
    submit = (By.NAME, 'submit')


    # 编辑用户
    def edit_user(self, **kwargs):
        # input username
        if kwargs.get('username', ''):
            self.input(kwargs['username'], *(By.NAME, 'username'))

        # select group
        if kwargs.get('level', ''):
            levels = kwargs['level'].split('.')
            for l in range(len(levels)):
                select = Select(self.get_element(By.XPATH, "//select[@level = {0}]".format(l + 1)))
                select.select_by_visible_text(levels[l])

        # select roleType
        if kwargs.get('roleType', 0):
            self.click(By.XPATH, '//input[@name="roleType" and @value="{0}"]'.format(kwargs['roleType']))

        # input name
        if kwargs.get('name', ''):
            self.input(kwargs['name'], *(By.NAME, 'name'))

        # input phone
        if kwargs.get('phone', ''):
            self.input(kwargs['phone'], *(By.NAME, 'phone'))

        # input wxaccount
        if kwargs.get('wxaccount', ''):
            self.input(kwargs['wxaccount'], *(By.NAME, 'wxaccount'))

        # input email
        if kwargs.get('email', ''):
            self.input(kwargs['email'], *(By.NAME, 'email'))

        # input remark
        if kwargs.get('remark', ''):
            self.input(kwargs['remark'], *(By.NAME, 'remark'))

        # input checkType
        if kwargs.get('checkType', ''):
            self.click(By.XPATH, '//input[@name=checkType and @value={0}]'.format(kwargs['checkType']))

        # input check reason
        if kwargs.get('checkreason', ''):
            self.input(kwargs['checkreason'], *(By.NAME, 'checkreason'))

    # 提交表单
    def submit_form(self):
        self.click(*self.submit)
        sleep(5)


    # 添加用户
    def add_user(self, **kwargs):
        # 点击"添加用户"按钮
        self.click(*self.add_new_user)

        # 输入用户信息
        self.edit_user(**kwargs)

        # 提交
        self.submit_form()



    # 添加组织架构
    def add_group(self, **kwargs):
        self.click(*self.add_new_group)

        # 输入 组织名
        if kwargs.get('name', ''):
            self.input(kwargs['name'], *(By.NAME, 'name'))
        else:
            assert False, "name don't set"

        # 选择 上级组织
        if kwargs.get('level', ''):
            levels = kwargs['level'].split('.')
            for l in range(len(levels)):
                select = Select(self.get_element(By.XPATH, "//select[@level = {0}]".format(l + 1)))
                select.select_by_visible_text(levels[l])
        else:
            assert False, "Level don't set"

        # 提交
        self.click(*self.submit)
        sleep(5)



