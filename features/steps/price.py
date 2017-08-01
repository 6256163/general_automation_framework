# coding=utf-8
import sys
from behave import *

from executer.execution import Execution
from page_object import store
from page_object.login import Login
from page_object.navigation import Navigation
from page_object.order import Order
from page_object.price import Price
from page_object.stock import Stock




@when('new a price')
def step_impl(context):
    context.price = Price(context.driver)
    context.price.new()


@when('fill and submit price form')
def step_impl(context):
    context.price.fill(**table_to_dict(context.table))


def sub_dict(dic, sub):
    return dict([(key, dic.get(key, None)) for key in sub])


def table_to_dict(table):
    dic = dict()
    for row in table:
        dic[row.cells[0]] = row.cells[1]
    return dic
