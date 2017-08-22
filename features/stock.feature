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
             |type|<type>|
             |date|<date>|
             |adr|<adr>|
             |area|<area>|
             |port|<port>|
        And add new
             |key|value|
             |store_slot|<store_slot>|
             |slot|<slot>|
             |submit|<submit>|
             |cpm|<cpm>|
        And fill
             |key|value|
             |adv|<adv>|
             |submit|提交|
        Then check list
             |key|value|
             |是否超量|<是否超量>|
        And store
             |order_in_storage|field|
             |<order_num>|订单编号|
        Examples: date
             |order_num|type|date|adr|area|port|store_slot|slot|submit|cpm|adv|是否超量|
             |order5|CPM|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京|客户端|1|1|加入|slot|六间房|否|
             |order5|CPM|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京|客户端|1|1|加入|slot;1|六间房|是|