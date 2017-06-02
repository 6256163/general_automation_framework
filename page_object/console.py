from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_object.base_page import BasePage


class Console(BasePage):
    def __init__(self, driver):
        super(Console, self).__init__(driver)

    add_new_user = (By.LINK_TEXT, '+添加新用户')
    add_new_group = (By.LINK_TEXT, '添加组织架构')
    submit = (By.NAME, 'submit')

    def user_form(self, **kwargs):

        self.click(*self.add_new_user)

        # input username
        if kwargs.get('username', ''):
            self.input(kwargs['username'], *(By.NAME, 'username'))
        else:
            assert False, "Username don't set"

        # select group
        if kwargs.get('level', ''):
            levels = kwargs['level'].split('.')
            for l in range(len(levels)):
                select = Select(self.get_element(By.XPATH, "//select[@level = {0}]".format(l + 1)))
                select.select_by_visible_text(levels[l])
        else:
            assert False, "Level don't set"

        # select roleType
        if kwargs.get('roleType', 0):
            self.click(By.XPATH, '//input[@name="roleType" and @value="{0}"]'.format(kwargs['roleType']))
        else:
            assert False, "Role type don't set"

        # input name
        if kwargs.get('name', ''):
            self.input(kwargs['name'], *(By.NAME, 'name'))
        else:
            assert False, "Name don't set"

        # input phone
        if kwargs.get('phone', ''):
            self.input(kwargs['phone'], *(By.NAME, 'phone'))
        else:
            assert False, "Phone don't set"

        # input wxaccount
        if kwargs.get('wxaccount', ''):
            self.input(kwargs['wxaccount'], *(By.NAME, 'wxaccount'))
        else:
            assert False, "WXaccount don't set"

        # input name
        if kwargs.get('email', ''):
            self.input(kwargs['email'], *(By.NAME, 'email'))
        else:
            assert False, "Email don't set"

        # input name
        if kwargs.get('remark', ''):
            self.input(kwargs['remark'], *(By.NAME, 'remark'))
        else:
            assert False, "Remark don't set"

        if kwargs.get('checkType', ''):
            self.click(By.XPATH, '//input[@name=checkType and @value={0}]'.format(kwargs['checkType']))


        if kwargs.get('checkreason', ''):
            self.input(kwargs['checkreason'], *(By.NAME, 'checkreason'))

        self.click(*self.submit)
        sleep(5)


    def group_form(self, **kwargs):
        self.click(*self.add_new_group)

        if kwargs.get('name', ''):
            self.input(kwargs['name'], *(By.NAME, 'name'))
        else:
            assert False, "name don't set"

        # select group
        if kwargs.get('level', ''):
            levels = kwargs['level'].split('.')
            for l in range(len(levels)):
                select = Select(self.get_element(By.XPATH, "//select[@level = {0}]".format(l + 1)))
                select.select_by_visible_text(levels[l])
        else:
            assert False, "Level don't set"

        self.click(*self.submit)
        sleep(5)



