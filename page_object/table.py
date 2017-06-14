# coding=utf-8
from __future__ import absolute_import
from time import sleep

from selenium.webdriver.common.by import By

from .base_page import BasePage

class Table(BasePage):
    def __init__(self, driver):
        super(Table, self).__init__(driver)

    pagination = (By.CSS_SELECTOR, 'ul.pagination')
    next_page = (By.LINK_TEXT, '下一页»')
    first_page = (By.LINK_TEXT, '首页')

    # 获取列元素 td
    def get_line(self, index, value):
        """
        :param index: 列标识符，数字，从0开始，表示第一列
        :param value: 行标识符，待匹配的值。
        :return: tr WebElement 
        """
        # 跳转首页
        first_page = self.get_elements(*self.first_page)
        if len(first_page):
            first_page[0].click()

        # 分页循环
        while True:
            trs = self.get_elements(By.TAG_NAME, 'tr')
            # 遍历所有tr
            for tr in trs[1:]:
                tds = tr.find_elements(By.TAG_NAME, 'td')
                if len(tds) and tds[index].text == value:
                    return tr
                else:
                    continue
            # 点击下一页
            next_page = self.get_elements(*self.next_page)
            if len(next_page):
                next_page[0].click()
                sleep(3)
            else:
                return None

    # 验证 tr yuansu
    def verify_column(self, **kwargs):
        """
        :param :kwargs['column']: 列标识符，数字，从0开始，表示第一列
        :param :kwargs['value']: 行标识符，待匹配的值。
        :return: 
        """
        tr = self.get_line(int(kwargs['column']), kwargs['value'])
        if not tr:
            assert False, "Cannot find line:{0}".format(kwargs['value'])

    # 行操作
    def edit_column(self, **kwargs):
        """
        :param :kwargs['column']: 列标识符，数字，从0开始，表示第一列
        :param :kwargs['value']: 行标识符，待匹配的值。
        :param :kwargs['action']: 操作类型，编辑，启用，禁止，审核……
        :param :kwargs['confirm']: 操作确认选项，True、False
        :return: 
        """
        # key is for csv, value is for web element
        confirm = {
            'TRUE': 0,
            'FALSE': 1
        }
        tr = self.get_line(int(kwargs['column']), kwargs['value'])
        if tr:
            # 定位操作列
            operation = tr.find_elements(By.XPATH, 'td')[-1]
            # 点击操作项
            operation.find_element(By.LINK_TEXT, kwargs['action']).click()

            # 判断是否需要二次确认
            if kwargs['action'] in ['删除', '禁止', '启用']:
                confirm_index = kwargs['confirm'].upper()
                pop_dialog = self.driver.find_element(By.CSS_SELECTOR, 'div.popover_bar')
                btns = pop_dialog.find_elements(By.XPATH, './*')
                btns[confirm[confirm_index]].click()
                sleep(3)
        else:
            assert False, "Cannot find column:{0}".format(kwargs['value'])

    # 过滤 操作
    def filter(self, **kwargs):
        """
        :param kwargs['type']:过滤器的label文本。来自UI
        :param kwargs['option']: 过滤器的具体选项。来自UI
        :return: 
        """
        labels = self.get_elements(By.TAG_NAME,'label')
        filter_label = None
        for label in labels:
            if label.text == kwargs['type']:
                filter_label = label
                break
        if filter_label:
            filter_option = filter_label.find_element(By.XPATH,'..').find_element(By.LINK_TEXT,kwargs['option'])
            if filter_option:
                filter_option.click()
                sleep(3)
            else:
                assert False, "Can not find filter option: {0}".format(kwargs['option'])
        else:
            assert False, "Can not find filter type: {0}".format(kwargs['type'])

    # 搜索 操作
    def search(self,**kwargs):
        """
        :param kwargs['type']: 搜索框input元素中的name属性值
        :param kwargs['value']: 待输入的值
        :return: 
        """
        search_input = self.get_element(By.XPATH,'//input[@name="{0}"]'.format(kwargs['type']))
        search_input.clear()
        search_input.send_keys(kwargs['value'])
        serarch_btn = self.get_element(By.CSS_SELECTOR,'button.serarchBtn')
        serarch_btn.click()
        sleep(3)