@chrome
Feature: Order-Schedule
    User can new price and audit price to make it switch to correct type and state.
    Background: Login
        When logout
        And login
             |key|value|
             |username|2|
             |password|123456|
             |verifycode|imqa|


    Scenario Outline: check schedule detail
        Given navigate
             |key|value|
             |菜单|order_list|
        When new
        And stock query
             |key|value|
             |类型|<类型>|
             # 投放时间 date|起始日期；结束日期| 说明：根据当前时间往后推3-6天
             |日期|0;0|
             |广告位|<广告位>|
             |地域|中国.江苏.南京|
             |端口|<端口>|
             |时段|<时段>|
             |考核|<考核>|
             |投放方式|<投放方式>|
             |监测|<监测>|
        And add new
             |key|value|
             |排期|0|
             |下单|加入|
             |投放量|111|
        And store order
             |orderno|
             |<orderno>|
        And fill
             |key|value|
             |名称 |<名称>|
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
        Then check schedule
             |key|value|
             |广告位|<广告位_排期>|
             |平台|<端口>|
             |地域|中国->江苏->南京|
             |分量类型|<分量类型>|
             |分量明细|<分量明细>|
        Examples: test data
             |类型|orderno|广告位|端口|时段|考核|投放方式|监测|名称|广告主|广告位_排期|分量类型|分量明细|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|1|nrc..1|111|百胜|通用前贴|0;0|111|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|1|reachmax..1|111|宝洁|通用前贴|0;0|111|
             |CPM|order4|网站页面广告.首页.网站首页弹窗|客户端||0|1|nrc..1|111|英超俱乐部|网站首页弹窗|0;0||
             |CPM|order4|视频广告.通用位置.通用前贴|网站||0|1|nrc..1|111|英超俱乐部|通用前贴|0;0|111|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|3||111|英超俱乐部|通用前贴|1;0|110|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|2||111|英超俱乐部|通用前贴|0;0|111|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|1|nrc..1|111|英超俱乐部|通用前贴|1;1|110|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|1|nrc..2|111|英超俱乐部|通用前贴|1;0|111|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|1||111|英超俱乐部|通用前贴|1;1|110|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端|1;3;5|0|1||111|英超俱乐部|通用前贴|1;0|110|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||1|1||111|三七玩|通用前贴|0;0|111|
             |CPM|order4|视频广告.通用位置.通用前贴|客户端||0|1||111|三七玩|通用前贴|1;1|110|


    Scenario: add schedule to a pre-order
        When new
        And stock query
             |key|value|
             |类型|CPM|
             |日期|3;6|
             |广告位|视频广告.通用位置.通用暂停|
             |地域|中国.江苏.南京|
             |端口|客户端|
        And add new
             |key|value|
             |订单|order4|
             |排期|1;2;3|
             |下单|编辑|
             |投放量|5|
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
             |提交|保存|

    Scenario: check schedule detail
        Given navigate
             |key|value|
             |菜单|order_list|
        # operate order
        And operate
             |key|value|
             |order|order4|
             |operation|编辑|
        # operate tg
        When operate tg
             |key|value|
             |操作|编辑排期/单价|
        Then check tg detail
             |广告位|通用暂停|
             |平台|客户端|
             |地域|中国->江苏->南京|
             |价格|0.00|
             # 排期 |起始日期；结束日期；具体第几天（从0开始）
             |排期|3;6;1.2.3|
             |下单量|CPM;5|
             |确认|确定|

