# coding=utf-8
from __future__ import absolute_import

from .operation import Operation


class Expect(Operation):

    def __init__(self, csv):
        super(Expect,self).__init__(csv)

    def verify(self):
        actual_result = self.get_property_value(self.csv['ExpectBy'], self.csv['ExpectLocation'],
                                                self.csv['ExpectProperty'])

        if actual_result != self.csv['ExpectValue']:
            assert False, u"Get wrong value:{0}. Expected:{1}".format(actual_result, self.csv['ExpectValue'])

    def compare(self):
        values = list()
        for by, value, property in zip(self.csv['ExpectBy'].split(';'), self.csv['ExpectLocation'].split(';'),
                                       self.csv['ExpectProperty'].split(';')):
            value = self.get_property_value(by, value, property)
            values.append(value)
        for i in range(len(values)):
            if values[0].lower() == values[i].lower():
                pass
            else:
                assert False, u"Compreation {0} are not equal".format(values)
