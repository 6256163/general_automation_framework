from operation import Operation
from analysis import Analysis
import codecs

class Test(object):
    frame_driver = None
    frame_flag = 0

    def __init__(self, driver):
        self.driver = driver


    def execute_tc(self, path):
        csv_datas = list()
        with codecs.open(path,'r','utf-8') as testcase:
            for line in testcase.readlines():
                csv_datas.append(line.strip('\n').split(','))
        for i, data in enumerate(csv_datas):
            if i > 0:
                tc_data = dict(zip(csv_datas[0], data))
                if tc_data['Action']:
                    self.execute_action(tc_data)
                if tc_data['Expect']:
                    self.verify_expect(tc_data)


    def execute_action(self, datas):
        operation = Operation(self.driver)
        analysis = Analysis()
        loc = analysis.get_loc(datas['ActionBy'],datas['ActionLocation'])

        if datas['Action'].upper() == "INPUTVALUE":
            operation.input_value(datas['ActionValue'], loc)
        elif datas['Action'].upper() == "OPENPAGE":
            operation.open_page(datas['ActionValue'])
        elif datas['Action'].upper() == "CLICK":
            operation.click(loc)
        elif datas['Action'].upper() == "SWITCHFRAME":
            pass
        else:
            pass


    def verify_expect(self, datas):
        operation = Operation(self.driver)
        analysis = Analysis()
        loc = analysis.get_loc(datas['ExpectBy'], datas['ExpectLocation'])

        if datas['Expect'].upper() == "VERIFY":
            operation.verify(datas['ExpectValue'], datas['ExpectProperty'], loc)
        elif datas['Expect'].upper() == "COMPARE":
            operation.compare(datas['ExpectBy'].split(';'),datas['ExpectLocation'].split(';'), datas['ExpectProperty'].split(';'))
        else:
            pass

