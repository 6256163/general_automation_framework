import os, time

import sys

from executer.execution import Execution
from page_object.login import Login
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.page_object import PageObject
from page_object.price import Price
from page_object.stock import Stock
from page_object.table import Table

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
from page_object import store

login_url = 'http://10.28.8.102/site/superentrance'


def before_all(context):
    # initialize the global store
    store._init()
    store.set_value("aaa", '111')


def before_feature(context, feature):
    # launch browser
    if 'chrome' in feature.tags:
        context.driver = Execution({'Browser': 'chrome'}).driver

    # login user
    context.login = Login(context.driver, url=login_url)
    context.login.login(**{'username': '2', 'password': '123456', 'verifycode': 'imqa'})

    # Navigate to feature page
    context.navigation = Navigation(context.driver)
    if feature.name == "Order":
        context.navigation.click_menu(**{'menu': 'order_list'})
    elif feature.name == 'Price':
        context.navigation.click_menu(**{'menu': 'price_list'})

    # Load page module
    if feature.name.lower() in ['order','price']:
        page = '.'.join(['page_object', context.feature.name.lower(), context.feature.name])
        context.operate = PageObject().get_instence(page)(context.driver)
    context.order = Order(context.driver)
    context.price = Price(context.driver)
    context.table_ = Table(context.driver)
    context.stock = Stock(context.driver)


def after_feature(context, feature):
    # close browser
    context.driver.quit()
