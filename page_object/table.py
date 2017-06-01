from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class Table(BasePage):
    def __init__(self, driver):
        super(Table, self).__init__(driver)

    pagination = (By.CSS_SELECTOR, 'ul.pagination')
    next_page = (By.LINK_TEXT, u'下一页')
    first_page = (By.LINK_TEXT, u'首页')
    colum={
        u'用户帐号':0,
        u'姓名':1,
        u'角色': 1,
        u'所属组织': 1,
        u'使用状态': 1,
        u'审核状态': 1,
        u'姓名': 1,
    }

    def get_line(self,name):
        """
        :param name: 使用每一行的唯一标识符定位。如，username，id，
        :return: tr or None
        """
        # 跳转首页
        first_page = self.get_elements(*self.first_page)
        if len(first_page):
            first_page[0].click()
        while True:
            tds = self.get_elements(By.TAG_NAME, 'td')
            for td in tds:
                if td.get_attribute('text') == name:
                    return td.parent()
            if self.page_to(self.next_page[1]):
                break

    def page_to(self, num):
        """
        :param num: 页数，首页/尾页，上一页/下一页
        :return: True：表示没有找到元素
        """
        pagination = self.driver.find_elements(*self.pagination)
        next_page = pagination.find_elements(by=By.LINK_TEXT,value=num)
        if len(next_page):
            next_page.click()
        else:
            return True

    def operate(self, name, operation):
        line = self.get_line(name)
        line.find_element(by=By.LINK_TEXT,value = operation).click()


    def verify_colum(self,name, index):
        tr = self.get_line(name)
        return tr