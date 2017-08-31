# coding=utf-8
from behave import *
from selenium.webdriver.common.by import By
from page_object import store
from features.steps.common import *
from features.steps.stock import *
from page_object.table import Table
from page_object.tg import TG


@when('logout')
def logout(context):
    context.login.logout()


@when('login')
def login(context):
    dic = table_to_dict(context.table)
    context.login.login(**dic)