from selenium.webdriver.common.by import By

class Analysis(object):
    
    def get_loc(self, by_, loc):
        if by_.upper() == "XPATH":
            return (By.XPATH,loc)
        elif by_.upper() == "ID":
            return (By.ID,loc)
        elif by_.upper() == "CSS_SELECTOR":
            return (By.CSS_SELECTOR,loc)
        elif by_.upper() == "TAG_NAME":
            return (By.TAG_NAME,loc)
        elif by_.upper() == "LINK_TEXT":
            return (By.LINK_TEXT,loc)
        elif by_.upper() == "NAME":
            return (By.NAME,loc)
        elif by_.upper() == "CLASS_NAME":
            return (By.CLASS_NAME,loc)
        elif by_.upper() == "PARTIAL_LINK_TEXT":
            return (By.PARTIAL_LINK_TEXT,loc)
        else:
            pass
