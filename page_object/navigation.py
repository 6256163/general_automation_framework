from page_object.base_page import BasePage


class Navigation(BasePage):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)

    dropdown_office_account_management = 