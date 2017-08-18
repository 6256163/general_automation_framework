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
from page_object.tg import TG


@when('new')
def new(context):
    context.operate.new()


@then('store')
@given('store')
def store_(context):
    for row in context.table.rows:
        key = row.cells[0]
        field = row.cells[1]
        value = ''
        if key[0:5] in ['order','price']:
            value = context.table_.get_field(field)
        elif key[0:2] in ['tg']:
            value = context.table_tg.get_field(field)
        store.set_value(key, value)


@when('fill')
@then('fill')
def fill(context):
    dic = table_to_dict(context.table)
    context.operate.fill(**dic)


@given('search')
@when('search')
@then('search')
def search(context):
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.table_.search(order_num)

@given('operate')
@when('operate')
def operate(context):
    dic = table_to_dict(context.table)
    context.table_.execute(dic.pop('operation'))
    context.operate.fill(**dic)

@when('operate tg')
def operate_tg(context):
    dic = table_to_dict(context.table)
    table_loc = (By.CSS_SELECTOR, 'table.schedule-datalist')
    th_loc = (By.CSS_SELECTOR, 'tr.schedule-in')
    context.table_tg = Table(context.driver, loc=table_loc, th=th_loc)
    context.table_tg.execute(dic.pop('operation'))


@then('check list')
def check_list(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
            context.table_.search(dic[key])
    result = context.table_.verify(**dic)
    assert not result, result


@then('check schedule')
def check_schedule(context):
    dic = table_to_dict(context.table)
    table_loc = (By.CSS_SELECTOR,'table.schedule-datalist')
    th_loc = (By.CSS_SELECTOR, 'tr.schedule-in')
    context.table_tg = Table(context.driver, loc=table_loc, th=th_loc)
    context.table_tg.verify(**dic)


@then('check tg detail')
def check_tg_detail(context):
    dic = table_to_dict(context.table)
    context.tg = TG(context.driver)
    context.tg.verify(**dic)

