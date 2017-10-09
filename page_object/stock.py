# coding=utf-8
from __future__ import absolute_import

import re
from time import sleep

import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object import store
from .base_page import BasePage
from .selector import Selector


class Stock(BasePage):
    def __init__(self, driver):
        super(Stock, self).__init__(driver)

    def switch_type(self, type):

        if type.upper() == 'CPT':
            stock_type = 'CPT库存报表'
        elif type.upper() == 'CPM':
            stock_type = 'CPM库存报表'
        else:
            stock_type = None
        ul = self.get_element(By.CSS_SELECTOR, 'ul.page_tabs')
        for li in ul.find_elements(By.TAG_NAME, 'li'):
            if li.text == stock_type:
                li.click()
                break
        self.wait_ajax_loading()

    # 选取投放日期
    def select_date(self, dates):
        d = dates.split(';')
        # 点击日期选择器
        self.click(By.CSS_SELECTOR, '#filterDatepicker .icon')
        # 输入起止时间
        self.input(int_to_date(d[0]), *(By.CSS_SELECTOR, 'input.start',))
        self.input(int_to_date(d[1]), *(By.CSS_SELECTOR, 'input.end',))
        # 点击确定
        self.click(By.CSS_SELECTOR, 'button.enter')


    def select_adr(self, items):
        ad_selector = self.driver.find_element(By.XPATH,'//input[@data-bind="value: adSlot.ids"]/following-sibling::button')
        for item in items.split(';'):
            ad_selector.click()
            select = Selector(self.driver)
            select.select(item.split('.'))

    def select_area(self, items):
        ad_selector = self.driver.find_element(By.XPATH, '//input[@data-bind="value: region.ids"]/following-sibling::button')
        for item in items.split(';'):
            ad_selector.click()
            select = Selector(self.driver)
            select.select(item.split('.'))

    def select_content(self, items):
        ad_selector = self.driver.find_element(By.XPATH, '//input[@data-bind="value: content.ids"]/following-sibling::button')
        for item in items.split(';'):
            ad_selector.click()
            select = Selector(self.driver)
            select.select(item.split('.'))


    def select_port(self, port):
        btn = self.driver.find_element(By.XPATH, '//li[@data-search-term="客户端"]/ancestor::td//button')
        btn.click()
        [self.get_element(By.XPATH, '//li[@data-search-term="{0}"]'.format(p)).click() for p in port.split(';')]
        btn.click()


    def select_time(self, time):
        btn = self.driver.find_element(By.XPATH, '//li[@data-search-term="01:00 ~ 02:00"]/ancestor::td//button')
        btn.click()
        [btn.find_element(By.XPATH, 'ancestor::td//input[@value="{0}"]'.format(p)).click() for p in time.split(';')]
        btn.click()


    def select_exam(self, exam):
        if exam == '0':
            self.click(By.XPATH, '//input[@value="0"][@name="followingExamType"]')
        else:
            self.click(By.XPATH, '//input[@value="1"][@name="followingExamType"]')
            exam = exam.split(';')
            [self.click(By.XPATH,'//ul[@class="followingExam_items"]//input[@value="{0}"]'.format(i)) for i in exam]
            if '-2' in exam:
                self.input('11',By.CSS_SELECTOR,'div.followingExam_customCRT input')
            if '-1' in exam:
                self.input('其他',By.CSS_SELECTOR,'div.followingExam_customTxt input')

    def select_throw(self,throw):
        sel = self.get_element(By.XPATH, '//select[@data-bind="value: throwForm"]')
        select = Select(sel)
        select.select_by_value(throw)



    def select_tracker(self,tracker):
        trackers = tracker.split(';')
        for t in trackers:
            t= t.split('.')
            # select parent tracker
            self.click(By.CSS_SELECTOR, 'div.tracker_item input[value="{0}"]'.format(t[0]))
            sleep(0.5)
            # select child tracker
            if t[1]:
                self.click(By.CSS_SELECTOR,
                        'div.tracker_item_more_{0} div.tracker_item_product div.mcpp-list'.format(t[0]))
                sleep(0.5)
                self.click(By.CSS_SELECTOR, 'div.mcpp-wrapper input[value="{0}:{1}"]'.format(t[0],t[1]))
                sleep(0.5)
            # select tracker position
            self.click(By.CSS_SELECTOR,
                        'div.tracker_item_more_{0} div.tracker_item_position div.mcpp-list'.format(t[0]))
            sleep(0.5)
            self.click(By.CSS_SELECTOR, 'div.mcpp-wrapper input[value="{0}:{1}"]'.format(t[0], t[2]))



    def switch_mode(self, key):

        mode = {
            '下单': 'mode_select',
            '查询': 'mode_view'
        }
        sleep(5)
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format(mode[key])))

    mode = {
        '下单': 'mode_select',
        '查询': 'mode_view'
    }

    def select_slot(self, slot):
        sleep(5)
        self.click(*(By.XPATH, '//label[@for="mode_select"]'))
        [self.click(By.CSS_SELECTOR,'tbody.ui-selectable tr td[data-index="{0}"]'.format(i)) for i in slot.split(';')]


    def store_slot(self, slot):
        slot_list = list()
        tr = self.get_element(By.CSS_SELECTOR, 'tbody.ui-selectable tr')
        indexs = slot.split(';')
        for i in indexs:
            cell = tr.find_element(By.XPATH, 'td[@data-index="{0}"]'.format(i))
            slot_list.append(cell.text)
        store.set_value('slot', slot_list)


    def get_slot(self, d):
        tr = self.get_element(By.CSS_SELECTOR, 'tbody.ui-selectable tr')
        cell = tr.find_element(By.XPATH, 'td[@data-index="{0}"]'.format(d))
        return cell.text

    def select_order(self, order):
        sel = self.get_element(By.CSS_SELECTOR, 'select.campaign_list')
        select = Select(sel)
        select.select_by_visible_text(order)

    def submit(self, submit):

        map = {
            '加入': 'createNewBtn',
            '编辑': 'editOneBtn'
        }
        btn = self.get_element(By.ID, map[submit])
        btn.click()


    def check_stock(self, **kwargs):
        actual = int(self.get_slot(kwargs['slot']))
        stock = sum(list(map(int,store.get_value('slot'))))
        amount = re.match(r'站内流量：(.*?[1-9])CPM', store.get_value(kwargs['component'])).group(1)
        expect = int(stock) - int(amount)
        if expect - actual not in [1,0]:
            return '{0},{1},{2}'.format(stock, amount, actual)


    def query(self, **kwargs):
        dic = {
            '类型': self.switch_type,
            '日期': self.select_date,
            '广告位': self.select_adr,
            '地域': self.select_area,
            '内容': self.select_content,
            '时段':self.select_time,
            '端口': self.select_port,
            '监测':self.select_tracker,
            '投放方式':self.select_throw,
            '考核':self.select_exam
        }
        self.wait_ajax_loading()
        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)

        self.click(*(By.CSS_SELECTOR, 'button.submitBtn'))
        self.wait_ajax_loading()
        sleep(3)

    def cpm_set(self,cpm):
        if cpm.startswith('slot') :
            store_slot = store.get_value('slot')
            add_slot = cpm.split(';')[1] if len(cpm.split(';'))>1 else '0'
            store_slot.append(add_slot)
            cpm = str(
                sum(
                    list(
                        map(int,store_slot)
                    )
                )
            )
        self.input(cpm, By.CSS_SELECTOR, 'div.cpm_set input')
        self.click(By.CSS_SELECTOR, 'div.btnbar button.enterBtn')

    def add_new(self, **kwargs):
        self.click(*(By.XPATH, '//label[@for="{0}"]'.format('mode_select')))
        dic = {
            '存储排期库存':self.store_slot,
            '排期': self.select_slot,
            '订单': self.select_order,
            '下单': self.submit,
            '投放量':self.cpm_set
        }
        for key, value in kwargs.items():
            if key in dic.keys():
                dic[key](value)


def int_to_date(num):
    try:
        d = int(num)
        date_ = datetime.datetime.now() + datetime.timedelta(days=d)
        num = date_.strftime('%Y-%m-%d')
    except ValueError:
        pass
    return num