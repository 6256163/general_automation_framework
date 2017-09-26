import json

import MySQLdb

from page_object import store
from page_object.base_page import BasePage


class Mail(BasePage):



    def verify_to(self,sql_data, value):
        actual = set(sql_data['to'].keys())
        expect = set(value.split(';'))
        # assert actual == expect, 'actual_to = {0}. expect_to = {1}'.format(actual,expect)
        if actual != expect:
            return "skip"

    def verify_cc(self,sql_data, value):
        actual = set(sql_data['cc'].keys()) if sql_data['cc'] != [] else ''
        expect = set(value.split(';')) if value != 'None' else ''
        # assert actual == expect, 'actual_cc = {0}. expect_cc = {1}'.format(actual,expect)
        if actual != expect:
            return "skip"

    def verify_subject(self, sql_data, value):
        contents = value.split(';')
        for i, c in enumerate(contents):
            if store.get_value(c) != None:
                contents[i] = store.get_value(c)
        expect = ''.join(contents)
        actual = sql_data['subject']
        # assert actual == expect, 'actual_cc = {0}. expect_cc = {1}'.format(actual,expect)
        if actual != expect:
            return "skip"

    def verify_mail(self,**kwargs):

        # get actual data from DB
        sql = "SELECT OperationData FROM simpQA.log_operation where Action='sendemail' and ID>{0} order by ID desc;"\
            .format(store.get_value(kwargs.pop('mailid')))
        db = MySQLdb.connect("10.200.44.60", "snow_cheng", "eaps0543", "simpQA")
        while True:
            cursor = db.cursor()
            cursor.execute(sql)
            datas = cursor.fetchall()
            cursor.close()
            if len(datas):
                break
        db.close()

        # verify function
        dic = {
            '发送': self.verify_to,
            '抄送': self.verify_cc,
            '主题': self.verify_subject,
        }

        result = False
        for data in datas:
            d = json.loads(data[0])
            l = list()
            for key, value in kwargs.items():
                r = dic[key](d, value)
                if r:
                    break
                else:
                    l.append(r)
            if len(l) == len(kwargs):
                result = True
                break
            else:
                continue
        assert result, 'can not get mail operation. to:{0}, cc{1}, subject:{2}'.\
            format(kwargs.get('to',''),kwargs.get('cc',''),kwargs.get('subject',''))





