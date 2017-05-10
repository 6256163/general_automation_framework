import os

from action import Action
from expect import Expect

class Execution(Action,Expect):
    
    def __init__(self, driver, csv):
        self.action = Action(driver, csv)
        self.expect = Expect(driver, csv)
        
        
    def execute(self):
        
        if self.csv['Action'].upper() == "INPUT_VALUE":
            self.action.input_value()

        elif self.csv['Action'].upper() == "OPEN_PAGE":
            if self.csv['ActionLocation'] == '':
                self.action.open_page()
            else:
                path = os.path.join(os.getcwd(), self.csv['ActionLocation'], self.csv['ActionValue'])
                self.action.open_page(r'file://'+path)

        elif self.csv['Action'].upper() == "CLICK":
            self.action.click()

        elif self.csv['Action'].upper() == "SWITCH_FRAME":
            if self.csv['ActionBy'] == '':
                self.driver.switch_to.frame(self.csv['ActionLocation'])
            else:
                self.driver.switch_to.frame(self.action.get_element())

        elif self.csv['Action'].upper() == "SWITCH_DEFAULT_CONTENT":
            self.driver.switch_to.default_content()

        elif self.csv['Action'].upper() == "SWITCH_PARENT_FRAME":
            self.driver.switch_to.parent_frame()

        elif self.csv['Action'].upper() == "SWITCH_WINDOW":
            self.action.switch_window()

        elif self.csv['Action'].upper() == "OPEN_NEW_PAGE":
            if self.csv['ActionValue'] != '':
                loc = self.csv['ActionValue']
            self.action.open_new_page()
            
        else:
            pass
        