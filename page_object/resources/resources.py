class Resources(object):
    def __init__(self):
        self.order = Order()

class Order(object):
    def __init__(self):
        self.NEW = ('link text', '我要下单',)
        self.ADJUST = ('xpath', '//button[contains(text(), "调整排期和单价")]',)
        self.ORDER_TYPE = ('id', 'order_orderType',)
        self.ORDER_NAME = ('id', 'order_orderName',)
        self.ADV = ('xpath', '//button[ @ title = "选择"]',)
        self.PRODUCT_LINE = ('id', 'order_productLine',)
        self.AMOUNT = ('id', 'order_orderAmount',)
        self.COST = ('id', 'order_orderCost')
        self.PAY_DATE = 'document.getElementById("order_payDate").value = "{0}"'
        self.ORDER_NUM = ('xpath', '//input[@name = "order[orderno]"]',)
        self.SUBMIT = ('xpath', '//input[@value = "提交"]',)
        self.AUDIT = ('xpath', '//input[@value = "审批"]',)
