@chrome
Feature:TG
    Scenario: Create a new order
        Given order
            |key|value|
            |menu|order_list|
            |type|CPT|
            |date|3;5|
            |adr|视频广告.通用位置.通用前贴|
            |mode|下单|
            |slot|1;2;3|
            |adv|六间房|
            |submit|提交|
        And store
            |order_in_storage|field|
            |order1|订单编号|
        And price
            |key|value|
            |menu|price_list|
            |adv|六间房  |
            |date|3;5   |
            |adr |视频广告.通用位置.通用前贴|
            |area|中国.江苏.南京|
            |port|客户端.Ipad|
            |price|500|
            |type |硬广|
            |submit|保存并提交审批|
        And store
            |order_in_storage|field|
            |price1|价格政策ID|
        When search
            |order_in_storage|
            |order1|
        And operate
            |key|value|
            |operation|编辑|