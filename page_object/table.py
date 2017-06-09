from time import sleep

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class Table(BasePage):
    def __init__(self, driver):
        super(Table, self).__init__(driver)

    pagination = (By.CSS_SELECTOR, 'ul.pagination')
    next_page = (By.LINK_TEXT, '下一页»')
    first_page = (By.LINK_TEXT, '首页')

    def get_line(self, index, value):
        """
        :param name: 使用每一行的唯一标识符定位。如，username，id，
        :return: tr or None
        """
        # 跳转首页
        first_page = self.get_elements(*self.first_page)
        if len(first_page):
            first_page[0].click()
        while True:
            trs = self.get_elements(By.TAG_NAME, 'tr')
            for tr in trs[1:]:
                tds = tr.find_elements(By.TAG_NAME, 'td')
                if len(tds) and tds[index].text == value:
                    return tds[index]
                else:
                    continue
            next_page = self.get_elements(*self.next_page)
            if len(next_page):
                next_page[0].click()
                sleep(3)
            else:
                return None

    def page_to(self, num):
        """
        :param num: 页数，首页/尾页，上一页/下一页
        :return: True：表示没有找到元素
        """
        pagination = self.driver.find_elements(*self.pagination)
        next_page = pagination.find_elements(by=By.LINK_TEXT, value=num)
        if len(next_page):
            next_page.click()
        else:
            return True


    def verify_column(self, **kwargs):
        td = self.get_line(int(kwargs['column']), kwargs['value'])
        if td:
            if td.text != kwargs['value']:
                assert False, "Wrong column value: {0}. Expect: {1}".format(td.text, kwargs['value'])
        else:
            assert False, "Cannot find column:{0}".format(kwargs['value'])

    def edit_column(self, **kwargs):
        # key is for csv, value is for web element
        action = {
            '编辑': '编辑',
            '禁止': '禁止',
            '启用': '启用',
            '删除': '删除',
            '审核': '审核'
        }
        confirm = {
            'TRUE': 0,
            'FALSE': 1
        }
        td = self.get_line(int(kwargs['column']), kwargs['value'])
        if td:
            operation = td.find_elements(By.XPATH, '../td')[-1]
            action_index = kwargs['action']
            operation.find_element(By.LINK_TEXT, action[action_index]).click()

            if kwargs['action'] in ['2', '3', '4']:
                confirm_index = kwargs['confirm'].upper()
                pop_dialog = self.driver.find_element(By.CSS_SELECTOR, 'div.popover_bar')
                btns = pop_dialog.find_elements(By.XPATH, './*')
                btns[confirm[confirm_index]].click()
        else:
            assert False, "Cannot find column:{0}".format(kwargs['value'])


