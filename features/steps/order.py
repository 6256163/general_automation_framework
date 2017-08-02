from behave import *

from page_object import store
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.page_object import PageObject
from page_object.table import Table


@when('new')
def step_impl(context):
    # page = '.'.join(['page_object', context.feature.name.lower(), context.feature.name])
    # context.operate = PageObject().get_instence(page)
    context.operate.new()


@then('store')
def step_impl(context):
    context.table_ = Table(context.driver)
    for row in context.table.rows:
        key = row.cells[0]
        field = row.cells[1]
        value = context.table_.get_field(field)
        store.set_value(key, value)


@when('fill')
def step_impl(context):
    dic = table_to_dict(context.table)
    page = '.'.join(['page_object', context.feature.name.lower(), context.feature.name])
    context.operate = PageObject().get_instence(page)
    context.operate.fill(**dic)


@given('search')
def step_impl(context):
    context.order = Order(context.driver)
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.table_ = Table(context.driver)
    context.table_.search(order_num)


@when('operate')
def step_impl(context):
    dic = table_to_dict(context.table)
    page = '.'.join(['page_object', context.feature.name.lower(), context.feature.name])
    context.operate = PageObject().get_instence(page)
    context.table_ = Table(context.driver)
    context.table_.execute(dic['operation'])
    context.operate.fill(**dic)


@then('check list')
def step_impl(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
    context.table_ = Table(context.driver)
    result = context.table_.verify(**dic)
    assert not result, result


@given('navigate')
def step_impl(context):
    context.navigation = Navigation(context.driver)
    context.navigation.click_menu(**table_to_dict(context.table))


def sub_dict(dic, sub):
    return dict([(key, dic.get(key, None)) for key in sub])


def table_to_dict(table):
    dic = dict()
    for row in table:
        dic[row.cells[0]] = row.cells[1]
    return dic
