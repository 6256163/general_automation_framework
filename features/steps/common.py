# coding=utf-8
from __future__ import absolute_import
import collections
from behave import *

from page_object import store
from page_object.navigation import Navigation


@when('navigate')
@given('navigate')
def navigate(context):
    dic = table_to_dict(context.table)
    context.navigation.navigate(**dic)


def sub_dict(dic, sub):
    return dict([(key, dic.get(key, None)) for key in sub])


def table_to_dict(table):
    dic = collections.OrderedDict()
    for row in table:
        # store not empty string
        if row['value']:
            dic[row['key']] = row['value']
    return dic

