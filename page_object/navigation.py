# coding=utf-8
from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class Navigation(BasePage):
    def __init__(self, driver):
        super(Navigation, self).__init__(driver)

    # 通用菜单选项
    office_account_management = (By.LINK_TEXT, u'公众号管理')
    index = (By.LINK_TEXT, u'首页')
    office_account_list = (By.LINK_TEXT, u'公众号列表')
    fans_analysis = (By.LINK_TEXT, u'粉丝分析')
    article_analysis = (By.LINK_TEXT, u'图文分析')
    fans_ranking_list = (By.LINK_TEXT, u'粉丝排行')
    article_ranking_list = (By.LINK_TEXT, u'文章排行')

    task_management = (By.LINK_TEXT, u'任务管理')
    task_material = (By.LINK_TEXT, u'任务素材')
    task_statistics = (By.LINK_TEXT, u'任务统计')
    tag_management = (By.LINK_TEXT, u'群组管理')

    console = (By.LINK_TEXT, u'控制台')
    user_management = (By.LINK_TEXT, u'用户管理')
    group_management = (By.LINK_TEXT, u'组织架构管理')

    def click_menu(self, **kwargs):
        # click menus
        if kwargs.get('menu', ''):
            menus= kwargs['menu'].split('.')
            for m in menus:
                self.click(By.LINK_TEXT,m)
        else:
            assert False, "menu don't set"
