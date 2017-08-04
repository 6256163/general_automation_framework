@chrome
Feature:TG
    Scenario: Create a new order
        Given order
             |key|value|
             |type|CPT|
             |date|2017-10-13;2017-10-16|
             |adr|视频广告.通用位置.通用前贴|
             |mode|下单|
             |slot|1;2;3|
             |adv|六间房|
             |submit|提交|
        And store
             |order_in_storage|field|
             |order1|订单编号|
