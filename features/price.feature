@chrome
Feature: Price
    User can new price and audit price to make it switch to correct type and state.

    Scenario Outline: Create a new price
        When new
        And fill
            |key|value|
            |adv|六间房  |
            |date|3;5   |
            |adr |视频广告.通用位置.通用前贴;视频广告.通用位置.通用暂停|
            |area|中国.江苏.南京;中国.浙江|
            |port|客户端.Ipad;客户端.Ipad|
            |price|500.1000;5.10|
            |type |硬广;贴片|
            |submit|保存并提交审批|
        Then store
             |order_in_storage|field|
             |<price_num>|价格政策ID|
        And check list
             |key|value|
             |price|<price_num>|
             |状态|审核中|
        Examples:
             |price_num|
             |price1|


    Scenario Outline: audit a price to complete
        Given search
             |order_in_storage|
             |price1|
        When operate
             |key|value|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |price|price1|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|state|
             |审批|审批|审核中|
             |审批|审批|审核中|
             |审批|审批|审核中|
             |审批|审批|审核中|
             |审批|审批|已生成|

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

