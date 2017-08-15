# coding=utf-8
import collections
from behave import *

from page_object import store
from page_object.navigation import Navigation


@given('navigate')
def navigate(context):
    context.navigation = Navigation(context.driver)
    context.navigation.click_menu(table_to_dict(context.table)['menu'])


def sub_dict(dic, sub):
    return dict([(key, dic.get(key, None)) for key in sub])


def table_to_dict(table):
    dic = collections.OrderedDict()
    for row in table:
        # store not empty string
        if row.cells[1]:
            dic[row.cells[0]] = row.cells[1]
    return dic

