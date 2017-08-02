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

    new_button = (By.LINK_TEXT, '新增价格政策')

    def new(self):
        self.wait_datalist_loading()
        self.click(*self.new_button)

    def fill(self, **kwargs):
        buttons = self.get_elements(By.TAG_NAME, 'button')

        def sql_query(self, sql):
            db = pymysql.connect("10.28.8.102", "snow_cheng", "eaps0543", "simpQA")
            db.set_charset('utf8')
            cursor = db.cursor()
            cursor.execute(sql)
            result = str(cursor.fetchall()[-1][0])
            return result

        db_store = {
            'adr': [],
            'area': []
        }

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
            # set adr
            for adr in kwargs['adr'].split(';'):
                get_button('选择广告位').click()
                select = Selector(self.driver)
                select.select(adr.split('.'))
                sql = "select id from ad_position where PositionName='{0}'".format(adr.split('.')[-1])
                ad_id = sql_query(sql)
                db_store['adr'].append(ad_id)
        else:
            # restore adr ID
            adrs = self.get_element(By.ID, 'choose_ad_content').text.replace(',',';').replace('->','.')
            for adr in adrs:
                sql = "select id from ad_position where PositionName='{0}'".format(adr.split('.')[-1])
                ad_id = sql_query(sql)
                db_store['adr'].append(ad_id)

        if kwargs.get('area', None):
            for area in kwargs['area'].split(';'):
                get_button('选择地域').click()
                selector = Selector(self.driver)
                selector.select(area.split('.'))
                id_ = ''
                for a in area.split('.'):
                    sql = "select id from area where Title='{0}'".format(a)
                    area_id = sql_query(sql)
                    id_ += area_id + '_'
                db_store['area'].append(id_[:-1])
        else:
            areas = self.get_element(By.ID, 'addresid').text
            for area_id in areas.split(','):
                db_store['adr'].append(area_id)


        if kwargs.get('port', None):
            table = Table(self.driver)
            for port, ad_id in zip(kwargs['port'].split(';'), db_store['adr']):
                sel = table.table.find_element(By.ID, 'plat' + ad_id)
                select = Select(sel)
                [select.select_by_visible_text(p) for p in port.split('.')]

        if kwargs.get('price', None):
            # adr 分广告位
            for ad_id, prices in zip(db_store['adr'], kwargs['price'].split(';')):
                # area 分地域
                if len(db_store['area']):
                    for area_id, price in zip(db_store['area'], prices.split('/')):
                        # step 分阶梯
                        [self.input(p, By.NAME, "appl{0}-{1}[{2}]".format(ad_id, area_id, str(i + 1))) for i,p in
                         enumerate(price.split('.'))]
                else:
                    for price in prices.split('/'):
                        # step 分阶梯
                        [self.input(p, By.NAME, "appl{0}-0{1}".format(ad_id, str(i + 1))) for p, i in
                         enumerate(price.split('.'))]

        if kwargs.get('type', None):
            table = Table(self.driver)
            for i, ad_type in enumerate(kwargs['type'].split(';')):
                if ad_type == '贴片':
                    input = table.table.find_element(By.ID, 'paster-' + str(i))
                else:
                    input = table.table.find_element(By.ID, 'hard-' + str(i))
                input.click()

        if kwargs.get('submit', None):
            self.click(By.XPATH, "//input[@value='{0}']".format(kwargs['submit']))
            self.confirm_dialog()
