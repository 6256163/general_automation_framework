# coding=utf-8
from behave import *

from executer.execution import Execution
from features import store
from page_object.login import Login
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.stock import Stock

login_url = 'http://10.28.8.102/site/superentrance'

@given('browser should be launched')
def step_impl(context):
    context.driver = Execution({'Browser': context.table.rows[0].cells[0]}).driver


@given('login page is opened')
def step_impl(context):
    context.login = Login(context.driver, url=login_url)


@when('input user login info and submit')
def step_impl(context):
    context.login.login(**table_to_dict(context.table))


@then('show the index page')
def step_impl(context):
    assert context.driver.current_url.endswith('/index'), "Wrong page after login: {0}".format(context.driver.url)


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
    assert not context.order.verify_list(**table_to_dict(context.table))

@then('storage order number')
def step_impl(context):
    context.order = Order(context.driver)
    key = context.table.rows[0].cells[0]
    field = '订单编号'
    value = context.order.get_field(field=field)
    store.set_value(key, value)
    order_num = store.get_value(key)


@given('an order')
def step_impl(context):
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.order.search_order(order=order_num)

@when('audit the order')
def step_impl(context):
    for i in range(context.table.rows[0].cells[0]):
        context.order.execute(operation='审批')
        context.order.fill(operation='审批')

def sub_dict(dic, sub):
    return dict([(key, dic.get(key,None)) for key in sub])


def table_to_dict(table):
    dic = dict()
    for row in table:
        dic[row.cells[0]] = row.cells[1]
    return dic
