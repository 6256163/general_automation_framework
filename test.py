from operation import Operation
from analysis import Analysis

class Test(object):


    def __init__(self, driver):
        self.driver = driver


    def execute_tc(self, path):
        csv_datas = list()
        with open(path) as testcase:
            for i, line in enumerate(testcase.readlines()):
                csv_datas.append(line.strip('\n').split(','))
        for i, data in enumerate(csv_datas):
            if i > 0:
                tc_data = dict(zip(csv_datas[0], data))
                self.execute_action(tc_data)
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
        else:
            pass


    def verify_expect(self, datas):
        operation = Operation(self.driver)
        analysis = Analysis()
        loc = analysis.get_loc(datas['ExpectBy'], datas['ExpectLocation'])

        if datas['Expect'].upper() == "VERIFY":
            operation.verify(datas['ExpectValue'], datas['ExpectProperty'], loc)
        elif datas['Expect'].upper() == "COMPARE":
            operation.open_page(datas['ExpectValue'])
        else:
            pass

