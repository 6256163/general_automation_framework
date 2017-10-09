# coding=utf-8
import re

from behave import *
from features.steps.common import *
from page_object import store


@when('stock query')
def stock_query(context):
    dic = table_to_dict(context.table)
    context.stock.query(**dic)


@when('add new')
def add_new(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
    context.stock.add_new(**dic)



@then('check stock')
def check_stock(context):
    dic = table_to_dict(context.table)
    result = context.stock.check_stock(**dic)
    assert not result, result