# coding=utf-8

import MySQLdb
import time
from behave import *

from features.steps.common import *
from features.steps.stock import *


@then('check mail')
def check_mail(context):
    dic = table_to_dict(context.table)
    result = context.mail.verify_mail(**dic)
    assert not result, result


@when('store mail id')
def store_mail_id(context):
    sql = "SELECT * FROM simpQA.log_operation where Action='sendemail' order by ID desc limit 1;"
    db = MySQLdb.connect("10.200.44.60", "snow_cheng", "eaps0543", "simpQA")
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()[0]
    db.close()
    for row in context.table:
        key = row.cells[0]
        store.set_value(key, data)