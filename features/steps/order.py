# coding=utf-8
from behave import *
from selenium.webdriver.common.by import By
from page_object import store
from features.steps.common import *
from features.steps.stock import *
from page_object.table import Table
from page_object.tg import TG


@when('new')
def new(context):
    context.operate.new()

@when('store')
@then('store')
@given('store')
def store_(context):
    for row in context.table.rows:
        key = row.cells[0]
        field = row.cells[1]
        value = ''
        if key[0:5] in ['order','price']:
            value = context.table_.get_field(field)
        elif key[0:2] in ['tg']:
            value = context.table_tg.get_field(field)
        store.set_value(key, value)


@when('store order')
def store_order(context):
    for row in context.table:
        key = row['orderno']
        value = context.order.get_orderno()
        store.set_value(key, value)

@when('fill')
@then('fill')
def fill(context):
    dic = table_to_dict(context.table)
    context.operate.fill(**dic)


@given('search')
@when('search')
@then('search')
def search(context):
    key = context.table.rows[0].cells[0]
    order_num = store.get_value(key)
    context.table_.search(order_num)

@given('operate')
@when('operate')
def operate(context):
    dic = table_to_dict(context.table)
    if 'order' in dic.keys():
        value = store.get_value(dic.pop('order'))
    elif 'price' in dic.keys():
        value = store.get_value(dic.pop('price'))
    else:
        value = ''
    context.table_.search(value)
    context.table_.execute(dic.pop('operation'))


@when('audit {times}')
def operate_times(context, times):
    [(operate(context),fill(context)) for i in range(int(times))]



@when('operate tg')
def operate_tg(context):
    dic = table_to_dict(context.table)
    table_loc = (By.CSS_SELECTOR, 'table.schedule-datalist')
    th_loc = (By.CSS_SELECTOR, 'tr.schedule-in')
    context.table_tg = Table(context.driver, table=table_loc, th=th_loc)
    context.table_tg.execute(dic.pop('operation'))


@then('check list')
def check_list(context):
    dic = table_to_dict(context.table)
    for key in ['order', 'price']:
        if dic.get(key, None):
            dic[key] = store.get_value(dic[key])
            context.table_.search(dic.pop(key))
    result = context.table_.verify(**dic)
    assert not result, result


def init_schedule_table(context):
    table_loc = (By.CSS_SELECTOR, 'table.schedule-datalist')
    th_loc = (By.XPATH, './tbody/tr[1]/td')
    context.table_tg = Table(context.driver, table=table_loc, th=th_loc)


@then('check schedule')
def check_schedule(context):
    dic = table_to_dict(context.table)
    init_schedule_table(context)
    context.table_tg.verify_tg(**dic)


@when('store tg colunm')
def store_tg_colunm(context):
    dic = table_to_dict(context.table)
    init_schedule_table(context)
    key = dic.pop('key')
    value = context.table_tg.get_tg_value(dic['column'])
    store.set_value(key,value)


@then('check tg detail')
def check_tg_detail(context):
    dic = table_to_dict(context.table)
    context.tg = TG(context.driver)
    context.tg.verify_ta(**dic)


@when('edit schedule')
def edit_schedule(context):
    dic = table_to_dict(context.table)
    table_loc = (By.CSS_SELECTOR, 'table.schedule-datalist')
    th_loc = (By.CSS_SELECTOR, 'tr.schedule-in')
    context.table_tg = Table(context.driver, table=table_loc, th=th_loc)
    context.table_tg.edit(**dic)


@given('store audit graph')
def store_audit_graph(context):
    dic = table_to_dict(context.table)
    key = dic.pop('key')
    value = context.audit.get_audit_num(**dic)
    store.set_value(key, value)


@then('check audit graph')
def check_audit_graph(context):
    dic = table_to_dict(context.table)
    keys = dic.pop('key').split(';')
    expect = int(store.get_value(keys[0]))+int(keys[1])
    actual = int(context.audit.get_audit_num(**dic))
    assert expect==actual, "expect = {0}, actual = {1}".format(expect,actual)


