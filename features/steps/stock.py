# coding=utf-8

from features.steps.common import *


@when('stock query')
def step_impl(context):
    params = table_to_dict(context.table)
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
