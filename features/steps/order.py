# coding=utf-8
import sys
from behave import *

from executer.execution import Execution
from page_object import store
from page_object.login import Login
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.stock import Stock

@given('navigate to page')
def step_impl(context):
    context.navigation = Navigation(context.driver)
    context.navigation.click_menu(**table_to_dict(context.table))


@when('click new order')
def step_impl(context):
    context.order = Order(context.driver)
    context.order.new()


@when('stock query')
def step_impl(context):
    params = table_to_dict(context.table)
    context.stock = Stock(context.driver)
    context.stock.switch_stock_type(**sub_dict(params, ['type']))
    context.stock.select_date(**sub_dict(params, ['date']))
    for index, value in sub_dict(params, ['0', '1', '2', '3']).items():
        if value != None:
            context.stock.select_item(**{'select': index, 'items': value})
    context.stock.query()


@when('select slot and create new order')
def step_impl(context):
    params = table_to_dict(context.table)
    context.stock.switch_mode(**sub_dict(params, ['mode']))
    context.stock.select_slot(**sub_dict(params, ['index']))


@when('fill and submit info')
def step_impl(context):
    context.order.fill(**table_to_dict(context.table))


@then('check the order info from order list')
def step_impl(context):
    result = context.order.verify_list(**table_to_dict(context.table))
    assert not result, result

@then('storage order number')
def step_impl(context):
    context.order = Order(context.driver)
    key = context.table.rows[0].cells[0]
    field = '订单编号'.encode('gbk').decode()
    cod = sys.getdefaultencoding()
    value = context.order.get_field(field=field)
    store.set_value(key, value)
    order_num = store.get_value(key)


@given('an order')
def step_impl(context):
    context.order = Order(context.driver)
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.order.search_order(order=order_num)

@when('audit the order')
def step_impl(context):
    dic = table_to_dict(context.table)
    context.order.execute(**dic)
    context.order.fill(**dic)

@then('close browser')
def step_impl(context):
    context.driver.quit()


def sub_dict(dic, sub):
    return dict([(key, dic.get(key,None)) for key in sub])


def table_to_dict(table):
    dic = dict()
    for row in table:
        dic[row.cells[0]] = row.cells[1]
    return dic
