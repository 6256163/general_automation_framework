@chrome
Feature: Price
    User can new price and audit price to make it switch to correct type and state.

    Background: Navigate to Order list page
        Given navigate
             |key|value|
             |菜单|price_list|

    Scenario Outline: Create a new price
        When new
        And fill
            |key|value|
            |广告主|<adv>|
            |生效时间|<date>|
            |广告位|<adr>|
            |地域|<area>|
            |端口|<port>|
            |价格|<price>|
            |购买类型|<type>|
            |提交|<submit>|
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
      
      
    Scenario Outline: audit a price to complete
        When operate
             |key|value|
             |price|<price>|
             |operation|<operation>|
        And fill
             |key|value|
             |提交|<submit>|
        Then check list
             |key|value|
             |price|<price>|
             |状态|<state>|
        Examples: Per-order
             |price|operation|submit|state|
             |price1|审批|审批|审核中|
             |price1|审批|审批|审核中|
             |price1|审批|审批|审核中|
             |price1|审批|审批|审核中|
             |price1|审批|审批|已生成|


    Scenario Outline: edit a price and save
        When operate
             |key|value|
             |price|price1|
             |operation|<operation>|
        And fill
             |key|value|
             |广告位|<adr>|
             |价格|<price>|
             |提交|<submit>|
        Then check list
             |key|value|
             |price|price1|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|state|adr|price|
             |编辑|保存|编辑中|;视频广告.通用位置.通用前贴|40.200|
             |提交||编辑中|||

