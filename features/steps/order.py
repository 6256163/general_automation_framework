from behave import *

from executer.execution import Execution
from page_object.login import Login


login_url = 'http://10.28.8.102/site/superentrance'

@given('browser should be launched')
def step_impl(context):
    context.driver = Execution({'Browser':context.table.rows[0].cells[0]}).driver


@given('login page is opened')
def step_impl(context):
    context.login = Login(context.driver, url = login_url)


@when('input user login info and submit')
def step_impl(context):
    context.login.login(**table_to_dict(context.table))


@then('show the index page')
def step_impl(context):
    assert context.driver.current_url.endswith('/index'), "Wrong page after login: {0}".format(context.driver.url)



@given('login user')
def step_impl(context):
    pass


def table_to_dict(table):
    dic = dict()
    for row in table:
        dic[row.cells[0]]=row.cells[1]
    return dic