@chrome
Feature: Order-Schedule
    User can new price and audit price to make it switch to correct type and state.

    Background: save an order
        Given navigate
             |key|value|
             |menu|order_list|
        When new
        And stock query
             |key|value|
             |type|CPT|
             |date|3;6|
             |adr|0/视频广告.通用位置.通用前贴|
             |area|1/中国.江苏.南京|
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

    Scenario Outline: add schedule to a pre-order
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
        Then check schedule
             |key|value|
             |submit|保存|
             |广告位|通用暂停|
             |平台|客户端|
             |地域|中国.江苏.南京|
             |下单量|1CPT|


        Examples: Per-order
