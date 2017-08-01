# coding=utf-8
import pymysql
import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object.base_page import BasePage
from page_object.selector import Selector
from page_object.table import Table


class Price(BasePage):
    def __init__(self, driver):
        super(Price, self).__init__(driver)
        self.wait_datalist_loading()


    def sql_query(self, sql):
        db = pymysql.connect("10.28.8.102", "snow_cheng", "eaps0543", "simpQA")
        db.set_charset('utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        return str(cursor.fetchone()[0])

    db_store = {
        'adr':[],
        'area':[]
    }
    new_button = (By.LINK_TEXT, '新增价格政策')

    def new(self):
        self.wait_datalist_loading()
        self.click(*self.new_button)



    def fill(self, **kwargs):

        buttons = self.get_elements(By.TAG_NAME, 'button')

        def get_button(btn_text):
            for b in buttons:
                if b.text == btn_text:
                    return b

        if kwargs.get('adv', None):
            get_button('选择广告主').click()
            select = Selector(self.driver)
            select.search(kwargs['adv'])
            sleep(3)

        if kwargs.get('from', None):
            date = kwargs['from']
            try:
                d = int(kwargs['from'])
                date_ = datetime.datetime.now() + datetime.timedelta(days=d)
                date = date_.strftime('%Y-%m-%d')
            except ValueError:
                pass
            self.driver.execute_script('document.getElementById("from").value="{0}"'.format(date))

        if kwargs.get('to', None):
            date = kwargs['to']
            try:
                d = int(kwargs['to'])
                date_ = datetime.datetime.now() + datetime.timedelta(days=d)
                date = date_.strftime('%Y-%m-%d')
            except ValueError:
                pass
            self.driver.execute_script('document.getElementById("to").value="{0}"'.format(date))

        if kwargs.get('adr', None):
            for adr in kwargs['adr'].split(';'):
                get_button('选择广告位').click()
                select = Selector(self.driver)
                select.select(adr.split('.'))
                sql = "select id from ad_position where PositionName='{0}'".format(adr.split('.')[-1])
                id = self.sql_query(sql)
                self.db_store['adr'].append(id)

        if kwargs.get('area', None):
            for area in kwargs['area'].split(';'):
                get_button('选择地域').click()
                select = Selector(self.driver)
                select.select(area.split('.'))
                id_ = ''
                for a in area.split('.'):
                    sql = "select id from area where Title='{0}'".format(a)
                    id = self.sql_query(sql)
                    id_ += id+'_'
                self.db_store['adr'].append(id_[:-1])

        if kwargs.get('port', None):
            table = Table(self.driver)
            for port, id in zip(kwargs['port'].split(';'), self.db_store['adr']):
                sel = table.table.find_element(By.ID, 'plat' + id)
                select = Select(sel)
                [select.select_by_visible_text(p) for p in port.split('.')]

        if kwargs.get('price', None):
            # adr 分广告位
            for ad_id, prices in zip(self.db_store['adr'], kwargs['price'].split(';')):
                # area 分地域
                if len(self.db_store['area']):
                    for area_id, price in zip(self.db_store['area'], prices.split('/')):
                        # step 分阶梯
                        [self.input(p, By.NAME, "appl{0}-{1}{2}".format(ad_id, area_id, str(i + 1))) for p, i in enumerate(price.split('.'))]
                else:
                    for price in prices.split('/'):
                        # step 分阶梯
                        [self.input(p, By.NAME, "appl{0}-0{1}".format(ad_id, str(i + 1))) for p, i in enumerate(price.split('.'))]

        if kwargs.get('type', None):
            table = Table(BasePage)
            for i, ad_type in enumerate(kwargs['type'].split(';')):
                if kwargs['type'] == '贴片':
                    input = table.table.find_element(By.ID, 'paster-' + str(i))
                else:
                    input = table.table.find_element(By.ID, 'hard-' + str(i))
                input.click()


        if kwargs.get('submit',None):
            self.get_element(By.XPATH,"//input[@value='{0}']".format(kwargs['submit']))
