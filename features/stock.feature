@chrome
Feature: Order-Stock
    The stock can reduce correctly according to the order

    Scenario Outline: check the stock reduce
        Given switch system
             |key|value|
             |type|视频|
        And navigate
             |key|value|
             |菜单|order_list|
        When new
        And stock query
             |key|value|
             |类型|<类型>|
             # 投放时间 date|起始日期；结束日期| 说明：根据当前时间往后推3-6天
             |日期|0;0|
             |广告位|<广告位>|
             |地域|中国.上海|
             |端口|<端口>|
             |时段|<时段>|
             |考核|<考核>|
             |投放方式|<投放方式>|
             |监测|<监测>|
        And add new
             |key|value|
             |存储排期库存|<slot>|
             |排期|0|
             |下单|加入|
             |投放量|111|
        And store order
             |orderno|
             |<orderno>|
        And fill
             |key|value|
             |名称 |111|
             |广告主|<广告主>|
             |提交|提交|
        And logout
        And login
             |key|value|
             |username|12070106|
             |password|123456|
             |verifycode|imqa|
        And navigate
             |key|value|
             |菜单|order_list|
        And operate
             |key|value|
             |order|<orderno>|
             |operation|审批|
        And store tg colunm
             |key|value|
             |key|<component>|
             |column|分量明细|
        And fill
             |key|value|
             |提交|审批|
        And logout
        And login
             |key|value|
             |username|2|
             |password|123456|
             |verifycode|imqa|
        And switch system
             |key|value|
             |type|视频|
        And navigate
             |key|value|
             |菜单|order_list|
        And audit <times>
             |key|value|
             |order|<orderno>|
             |operation|审批|
             |提交|审批|
        And operate
             |key|value|
             |order|<orderno>|
             |operation|编辑|
        And fill
             |key|value|
             |预计支付|1|
             |提交|提交|
        And navigate
             |key|value|
             |菜单|stock_booked|
        And stock query
             |key|value|
             |类型|<类型>|
             # 投放时间 date|起始日期；结束日期| 说明：根据当前时间往后推3-6天
             |日期|0;0|
             |广告位|<广告位>|
             |地域|中国.上海|
             |端口|<端口>|
             |时段|<时段>|
             |考核|<考核>|
             |投放方式|<投放方式>|
             |监测|<监测>|
        Then check stock
             |key|value|
             |slot|<slot>|
             |component|<component>|
        Examples: test data
             |类型|orderno|slot|component|广告位|端口|时段|考核|投放方式|监测|广告主|times|
             |CPM|order4|0|component1|视频广告.通用位置.通用前贴|客户端||0|1|nrc..1|百胜|1|
             |CPM|order4|0|component1|视频广告.通用位置.通用前贴|客户端||0|3||英超俱乐部|1|
             |CPM|order4|0|component1|视频广告.通用位置.通用前贴|客户端||0|1|nrc..1|英超俱乐部|1|
