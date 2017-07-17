# coding=utf-8
from __future__ import absolute_import

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage

class Navigation(BasePage):
    def __init__(self, driver):
        super(Navigation, self).__init__(driver)

    # 一级 - 首页菜单
    index = [(By.PARTIAL_LINK_TEXT,'首页')]
    # 一级 - 订单管理菜单
    order = (By.PARTIAL_LINK_TEXT,'订单管理')
    # 二级 - 订单列表
    order_list = [order, (By.PARTIAL_LINK_TEXT,'订单列表')]
    # 二级 - 订单审核概览
    order_audit = [order, (By.PARTIAL_LINK_TEXT,'订单审核概览')]
    # 二级 - 价格政策列表
    price_list = [order, (By.PARTIAL_LINK_TEXT,'价格政策列表')]
    # 二级 - 价格政策审批概览
    price_audit = [order, (By.PARTIAL_LINK_TEXT,'价格政策审批概览')]
    # 一级 - 资源管理
    source = (By.PARTIAL_LINK_TEXT,'资源管理')
    # 二级 - 库存预定
    stock_booked = [source, (By.PARTIAL_LINK_TEXT,'库存预定')]
    # 二级 - 库存设置
    stock_set = [source, (By.PARTIAL_LINK_TEXT,'库存设置')]
    # 一级 - 数据报表
    report = (By.PARTIAL_LINK_TEXT,'数据报表')
    # 二级 - 广告销售报表
    order_report = [report, (By.PARTIAL_LINK_TEXT,'广告销售报表')]
    # 二级 - 媒体资源报表
    ad_report = [report, (By.PARTIAL_LINK_TEXT,'媒体资源报表')]
    # 一级 - 系统管理
    system = (By.PARTIAL_LINK_TEXT,'系统管理')
    # 二级 - 用户管理
    user_list = [system, (By.PARTIAL_LINK_TEXT,'用户管理')]
    # 二级 - 角色管理
    role_list = [system, (By.PARTIAL_LINK_TEXT,'角色管理')]
    # 二级 - 订单审批设置
    order_process = [system, (By.PARTIAL_LINK_TEXT,'订单审批设置')]
    # 二级 - 议价审批设置
    price_process = [system, (By.PARTIAL_LINK_TEXT,'议价审批设置')]
    # 一级 - 易购资源
    suning = (By.PARTIAL_LINK_TEXT,'易购资源')
    # 二级 - 库存报表
    stock_report = [suning, (By.PARTIAL_LINK_TEXT,'库存报表')]
    # 二级 - 价格政策管理
    price_policy = [suning, (By.PARTIAL_LINK_TEXT,'价格政策管理')]

    def click_menu(self, **kwargs):
        # click menus
        if kwargs.get('menu', False):
            menus= getattr(Navigation,kwargs['menu'])
            for m in menus:
                self.click(*m)
        else:
            assert False, "menu don't set"
