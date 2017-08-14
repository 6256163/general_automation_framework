# coding=utf-8
from time import sleep

from behave import *
from selenium.webdriver.common.by import By

from page_object import store
from features.steps.common import *
from features.steps.stock import *
from page_object.order import Order
from page_object.page_object import PageObject
from page_object.price import Price
from page_object.table import Table


@when('new')
def new_when(context):
    context.operate.new()


@then('store')
@given('store')
def store_then(context):
    for row in context.table.rows:
        key = row.cells[0]
        field = row.cells[1]
        value = context.table_.get_field(field)
        store.set_value(key, value)


@when('fill')
@then('fill')
def fill_when(context):
    dic = table_to_dict(context.table)
    context.operate.fill(**dic)


@given('search')
@when('search')
@then('search')
def search_given(context):
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.table_.search(order_num)


@when('operate')
def operate_when(context):
    dic = table_to_dict(context.table)
    context.table_.execute(dic.pop('operation'))
    context.operate.fill(**dic)


@then('check list')
def check_list_then(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
            context.table_.search(dic[key])
    result = context.table_.verify(**dic)
    assert not result, result


@then('check schedule')
def check_schedule_then(context):
    dic = table_to_dict(context.table)
    table_loc = (By.CSS_SELECTOR,'table.schedule-datalist')
    th_loc = (By.CSS_SELECTOR, 'tr.schedule-in')
    context.table_ = Table(context.driver, loc=table_loc, th=th_loc)
    context.table_.verify(**dic)

