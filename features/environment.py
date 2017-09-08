# coding=utf-8
from __future__ import unicode_literals
import os
import sys, platform

from selenium import webdriver

import setting
from executer.execution import Execution
from page_object import PageObject
from page_object.login import Login
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.price import Price
from page_object.stock import Stock
from page_object.table import Table

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
from page_object import store

login_url = 'http://10.200.44.43/site/superentrance'
# login_url = 'http://10.28.8.102/site/superentrance'


def before_all(context):
    # initialize the global store
    store._init()
    store.set_value("aaa", '111')
    # context.config.setup_logging()


def before_feature(context, feature):
    if platform.platform().startswith("Win"):
        suffix = '.exe'
    else:
        suffix = ''
    # launch browser
    if 'chrome' in feature.tags:
        opt = webdriver.ChromeOptions()
        opt.add_argument('--start-maximized')
        opt.add_argument('--lang=zh-CN')
        context.driver = webdriver.Remote("http://0.0.0.0:32770/wd/hub", opt.to_capabilities().copy())
        context.driver.set_window_size(1440, 900)

        # driver_path = os.path.join(setting.BROWSER_DRIVER_FOLDER, 'chromedriver' + suffix)
        # os.environ["webdriver.chrome.driver"] = driver_path
        # context.driver = webdriver.Chrome(driver_path)
        # context.driver = Execution({'Browser': 'chrome'}).driver
        # context.driver = webdriver.PhantomJS('phantomjs')

    try:
        context.driver.maximize_window()
    except:
        pass


    # login user
    context.login = Login(context.driver, url=login_url)
    context.login.login(
        username='2',
        password='123456',
        verifycode='imqa'
    )
    context.driver.save_screenshot('/Users/tianzhang/Downloads/google111.png')

    # Load page module
    obj = feature.name[0:5]
    page = '.'.join(['page_object', obj.lower(), obj])
    context.operate = PageObject().get_instence(page)(context.driver)
    context.navigation = Navigation(context.driver)
    context.order = Order(context.driver)
    context.price = Price(context.driver)
    context.table_ = Table(context.driver)
    context.stock = Stock(context.driver)


def after_feature(context, feature):
    # close browser
    context.driver.quit()


def before_scenario(context, scenario):
    if 'need_background ' in scenario.tags:
        context.if_background = True
    else:
        context.if_background = False
