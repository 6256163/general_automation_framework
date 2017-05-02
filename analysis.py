from selenium.webdriver.common.by import By

class Analysis(object):
    
    def get_loc(self, by_, loc):
        if by_.upper() == "XPATH":
            return {'by':By.XPATH,'value':loc}
        elif by_.upper() == "ID":
            return {'by':By.ID,'value':loc}
        elif by_.upper() == "CSS_SELECTOR":
            return {'by':By.CSS_SELECTOR,'value':loc}
        elif by_.upper() == "TAG_NAME":
            return {'by':By.TAG_NAME,'value':loc}
        elif by_.upper() == "LINK_TEXT":
            return {'by':By.LINK_TEXT,'value':loc}
        elif by_.upper() == "NAME":
            return {'by':By.NAME,'value':loc}
        elif by_.upper() == "CLASS_NAME":
            return {'by':By.CLASS_NAME,'value':loc}
        elif by_.upper() == "PARTIAL_LINK_TEXT":
            return {'by':By.PARTIAL_LINK_TEXT,'value':loc}
        else:
            pass

    def get_compare(self, expectBy, expectLocation):
        bys = expectBy.split(';')
        locs = expectLocation.split(';')
        return [self.get_loc(bys[0],locs[0]),self.get_loc(bys[1],locs[1])]