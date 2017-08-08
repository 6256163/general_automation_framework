@chrome
Feature: Price
    User can new price and audit price to make it switch to correct type and state.

    Scenario Outline: Create a new price
        When new
        And fill
            |key|value|
            |adv|<adv>|
            |date|<date>|
            |adr |<adr>|
            |area|<area>|
            |port|<port>|
            |price|<price>|
            |type |<type>|
            |submit|<submit>|
        Then store
             |order_in_storage|field|
             |<price_num>|价格政策ID|
        And check list
             |key|value|
             |price|<price_num>|
             |状态|<状态>|
        Examples:
             |price_num|adv|date|adr|area|port|price|type|submit|状态|
             |price1|六间房|3;6|视频广告.通用位置.通用前贴;视频广告.通用位置.通用暂停|中国.江苏.南京;中国.浙江|客户端.Ipad;客户端.Ipad|500.1000;5.10|硬广;贴片|保存并提交审批|审核中|
             |price2|六间房|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京;中国.浙江|客户端.Ipad|500.1000|硬广|保存并提交审批|审核中|
             |price3|六间房|3;6|视频广告.通用位置.通用暂停|中国.江苏.南京;中国.浙江|客户端.Ipad|500.1000|硬广|保存并提交审批|审核中|
             |price4|六间房|3;6|视频广告.通用位置.通用前贴|中国.浙江|客户端.Ipad|500|硬广|保存并提交审批|审核中|
             |price5|六间房|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京;中国.浙江|客户端|500.1000|硬广|保存并提交审批|审核中|
             |price6|六间房|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京;中国.浙江|客户端.Ipad|500.1000|贴片|保存并提交审批|审核中|

      
      
    Scenario Outline: audit a price to complete
        Given search
             |order_in_storage|
             |<price>|
        When operate
             |key|value|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |price|price1|
             |状态|<state>|
        Examples: Per-order
             |price|operation|submit|state|
             |price1|审批|审批|审核中|
             |price1|审批|审批|审核中|
             |price1|审批|审批|审核中|
             |price1|审批|审批|审核中|
             |price1|审批|审批|已生成|
             |price2|审批|审批|审核中|
             |price2|审批|审批|审核中|
             |price2|审批|审批|审核中|
             |price2|审批|审批|审核中|
             |price2|审批|审批|已生成|
             |price3|审批|审批|审核中|
             |price3|审批|审批|审核中|
             |price3|审批|审批|审核中|
             |price3|审批|审批|审核中|
             |price3|审批|审批|已生成|
             |price4|审批|审批|审核中|
             |price4|审批|审批|审核中|
             |price4|审批|审批|审核中|
             |price4|审批|审批|审核中|
             |price4|审批|审批|已生成|
             |price5|审批|审批|审核中|
             |price5|审批|审批|审核中|
             |price5|审批|审批|审核中|
             |price5|审批|审批|审核中|
             |price5|审批|审批|已生成|
             |price6|审批|审批|审核中|
             |price6|审批|审批|审核中|
             |price6|审批|审批|审核中|
             |price6|审批|审批|审核中|
             |price6|审批|审批|已生成|

        Scenario Outline: edit a price and save
        Given search
             |order_in_storage|
             |price1|
        When operate
             |key|value|
             |price|<price>|
             |adr|<adr>|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |price|price1|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|state|adr|price|
             |编辑|保存|编辑中|;视频广告.通用位置.通用前贴|40.200|
             |提交||审核中|||

