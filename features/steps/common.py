# coding=utf-8
import collections
from behave import *
from page_object.navigation import Navigation


@given('navigate')
def navigate_given(context):
    context.navigation = Navigation(context.driver)
    context.navigation.click_menu(**table_to_dict(context.table))


def sub_dict(dic, sub):
    return dict([(key, dic.get(key, None)) for key in sub])


def table_to_dict(table):
    dic = collections.OrderedDict()
    for row in table:
        dic[row.cells[0]] = row.cells[1]
    return dic
