# coding=utf-8
from behave import *
from features.steps.common import *


@when('stock query')
def stock_query_when(context):
    dic = table_to_dict(context.table)
    context.stock.query(**dic)


@when('add new')
def add_new_when(context):
    dic = table_to_dict(context.table)
    context.stock.add_new(**dic)
