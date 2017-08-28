@chrome
Feature: Order-Schedule
    User can new price and audit price to make it switch to correct type and state.

    Scenario: save an order
        Given navigate
             |key|value|
             |menu|order_list|
        When new
        And stock query
             |key|value|
             |type|CPT|
             # 投放时间 date|起始日期；结束日期| 说明：根据当前时间往后推3-6天
             |date|3;6|
             |adr|视频广告.通用位置.通用前贴|
             |area|中国.江苏.南京|
             |port|客户端|
        And add new
             |key|value|
             |slot|1;2;3|
             |submit|加入|
        And fill
             |key|value|
             |adv|六间房|
             |submit|保存|
        Then check list
             |key|value|
             |类型|询量|
             |状态|编辑中|
        And store
             |order_in_storage|field|
             |order4|订单编号|

    Scenario: add schedule to a pre-order
        When new
        And stock query
             |key|value|
             |type|CPM|
             |date|3;6|
             |adr|0/视频广告.通用位置.通用暂停|
             |area|1/中国.江苏.南京|
             |port|客户端|
        And add new
             |key|value|
             |order|order4|
             |slot|1;2;3|
             |submit|编辑|
             |cpm |5|
        Then check schedule
             |key|value|
             |广告位|通用暂停|
             |平台|客户端|
             |地域|中国->江苏->南京|
             |下单量|5CPM|
        And store
             |order_in_storage|field|
             |tg1|编号|
        And fill
             |key|value|
             |submit|保存|

    Scenario: check schedule detail
        Given navigate
             |key|value|
             |menu|order_list|
        And search
             |order_in_storage|
             |order4          |
        # operate order
        And operate
             |key|value|
             |operation|编辑|
        # operate tg
        When operate tg
             |key|value|
             |operation|编辑排期/单价|
        Then check tg detail
             |广告位|通用暂停|
             |平台|客户端|
             |地域|中国->江苏->南京|
             |价格|0.00|
             # 排期 |起始日期；结束日期；具体第几天（从0开始）
             |排期|3;6;1.2.3|
             |下单量|CPM;5|
             |submit|确定|

