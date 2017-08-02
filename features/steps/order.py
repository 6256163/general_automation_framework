# coding=utf-8
from page_object import store
from features.steps.common import *
from page_object.order import Order


@when('new')
def step_impl(context):
    context.operate.new()


@then('store')
def step_impl(context):
    for row in context.table.rows:
        key = row.cells[0]
        field = row.cells[1]
        value = context.table_.get_field(field)
        store.set_value(key, value)


@when('fill')
def step_impl(context):
    dic = table_to_dict(context.table)
    context.operate.fill(**dic)


@given('search')
def step_impl(context):
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.table_.search(order_num)


@when('operate')
def step_impl(context):
    dic = table_to_dict(context.table)
    context.table_.execute(dic['operation'])
    context.operate.fill(**dic)


@then('check list')
def step_impl(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
    result = context.table_.verify(**dic)
    assert not result, result
