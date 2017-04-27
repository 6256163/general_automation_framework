from operation import Operation


class Action:

    def execute_tc(self, path):
        with open(path) as testcase:
            arg_name = list()
            for i, line in enumerate(testcase.readlines()):
                if i == 0:
                    arg_name = line.split(',')
                else:
                    tc_args = dict(zip(arg_name, line.split(',')))
                    self.execute_action(tc_args)


    def execute_action(self, **datas):
        operation = Operation()

        if str(datas['Action']).upper() == "INPUTVALUE":
            operation.input_value()




if __name__ == "__main__":
    a = Action()
    a.get_data(r'D:\study\general_automation_framework\testcase.csv')