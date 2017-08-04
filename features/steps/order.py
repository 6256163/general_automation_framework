# coding=utf-8
from behave import *
from page_object import store
from features.steps.common import *
from features.steps.stock import *


@given('order')
def order_given(context):
    new_when(context)
    stock_query_when(context)
    add_new_when(context)
    fill_when(context)




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
def fill_when(context):
    dic = table_to_dict(context.table)
    context.operate.fill(**dic)


@given('search')
def search_given(context):
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.table_.search(order_num)


@when('operate')
def operate_when(context):
    dic = table_to_dict(context.table)
    context.table_.execute(dic['operation'])
    context.operate.fill(**dic)


@then('check list')
def check_list_then(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
    result = context.table_.verify(**dic)
    assert not result, result
