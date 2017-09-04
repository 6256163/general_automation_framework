@chrome
Feature: Order-Stock
    User can new price and audit price to make it switch to correct type and state.

    Scenario Outline: under stock limit
        Given navigate
             |key|value|
             |menu|order_list|
        When new
        And stock query
             |key|value|
             |类型|<type>|
             |日期|<date>|
             |广告位|<adr>|
             |地域|<area>|
             |端口|<port>|
        And add new
             |key|value|
             |store_slot|<slot>|
             |排期|<slot>|
             |下单|<submit>|
             |投放量|<cpm>|
        And fill
             |key|value|
             |广告主|<adv>|
             |提交|提交|
        Then check list
             |key|value|
             |是否超量|<是否超量>|
        And store
             |order_in_storage|field|
             |<order_num>|订单编号|
        Examples: date
             |order_num|type|date|adr|area|port|slot|submit|cpm|adv|是否超量|
             |order5|CPM|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京|客户端|1|加入|slot|六间房|否|
             |order5|CPM|3;6| 视频广告.通用位置.通用前贴|中国.江苏.南京|客户端|1|加入|slot;1|六间房|是|