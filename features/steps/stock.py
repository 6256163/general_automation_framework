# coding=utf-8
from behave import *
from page_object import store
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.stock import Stock
from page_object.page_object import PageObject



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


def sub_dict(dic, sub):
    return dict([(key, dic.get(key, None)) for key in sub])


def table_to_dict(table):
    dic = dict()
    for row in table:
        dic[row.cells[0]] = row.cells[1]
    return dic
