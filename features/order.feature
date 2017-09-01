@chrome
Feature: Order
    User can new order and audit order to make it switch to correct type and state.

    Background: Navigate to Order list page
        Given navigate
             |key|value|
             |菜单|order_list|

    Scenario Outline: Create a new order
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
             |slot|<slot>|
             |submit|加入|
        And store order
             |orderno|
             |<order_num>|
        And fill
             |key|value|
             |adv|<adv>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|<order_num>|
             |类型|<类型>|
             |状态|<状态>|

        Examples: order number
             |order_num|submit|type|date|adr|area|port|slot|adv|类型|状态|
             |order1|提交|CPT|3;6|视频广告.通用位置.通用前贴|中国.江苏.南京|客户端|1;2;3|六间房|询量|审批中|
             |order2|提交|CPT|3;6|视频广告.通用位置.通用暂停|中国.江苏.南京|客户端|1;2;3|六间房|询量|审批中|
             |order3|提交|CPT|3;6|视频广告.通用位置.通用前贴||客户端|1;2;3|六间房|询量|审批中|


    Scenario Outline: audit a pre-order to complete
        Given search
             |order_in_storage|
             |order1          |
        When operate
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|order1|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|type|state|amount|cost|pay_date|
             |审批|审批|询量|审批中||||
             |审批|审批|新设|待下单||||
             |编辑|提交|新设|审批中|100|200|2|
             |审批|审批|新设|审批中||||
             |审批|审批|新设|审批中||||
             |审批|审批|新设|已生成||||



    Scenario Outline: adjust an order to complete
        Given search
             |order_in_storage|
             |order2       |
        When operate
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|order2|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|type|state|amount|cost|pay_date|
             |审批|审批|询量|审批中||||
             |审批|审批|新设|待下单||||
             |编辑|提交|新设|审批中|100|200|2|
             |审批|审批|新设|审批中||||
             |审批|审批|新设|审批中||||
             |审批|审批|新设|已生成||||
             |调整|保存|调整|待下单|300|300|5|
             |编辑|提交|调整|审批中||||
             |审批|审批|调整|审批中||||
             |审批|审批|调整|审批中||||
             |审批|审批|调整|已生成||||

    Scenario Outline: cancel an order
        Given search
             |order_in_storage|
             |order3          |
        When operate
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|order3|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|type|state|amount|cost|pay_date|
             |审批|审批|询量|审批中||||
             |审批|审批|新设|待下单||||
             |编辑|提交|新设|审批中|100|200|2|
             |审批|审批|新设|审批中||||
             |审批|审批|新设|审批中||||
             |审批|审批|新设|已生成||||
             |撤销||撤销|编辑中||||
             |编辑|提交|撤销|审批中||||
             |审批|审批|撤销|审批中||||
             |审批|审批|撤销|审批中||||
             |审批|审批|撤销|审批中||||
             |审批|审批|撤销|审批中||||
             |审批|审批|撤销|审批中||||
             |审批|审批|撤销|审批中||||
             |审批|审批|撤销|已生成||||


    Scenario Outline: adjust an adjusted order
        Given search
             |order_in_storage|
             |order2        |
        When operate
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |adjust  |<adjust>  |
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|order2|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|type|state|amount|cost|pay_date|adjust|
             |调整|提交|调整|审批中||||调整排期和单价|
             |审批|审批|调整|审批中|||||
             |审批|审批|调整|待下单|||||
             |编辑|提交|调整|审批中|||||
             |审批|审批|调整|审批中|||||
             |审批|审批|调整|审批中|||||
             |审批|审批|调整|已生成|||||

    Scenario Outline: adjust order's schedule
        Given search
             |order_in_storage|
             |order1         |
        When operate
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |adjust  |<adjust>  |
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|order1|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|type|state|amount|cost|pay_date|adjust|
             |调整|保存|调整|编辑中||||调整排期和单价|
             |编辑|提交|调整|审批中|||||
             |审批|审批|调整|审批中|||||
             |审批|审批|调整|待下单|||||
             |编辑|提交|调整|审批中|300|500|3||
             |审批|审批|调整|审批中|||||
             |审批|审批|调整|审批中|||||
             |审批|审批|调整|已生成|||||


    Scenario Outline: cancel an adjusted order
        Given search
             |order_in_storage|
             |order1         |
        When operate
             |key|value|
             |operation|<operation>|
             |submit|<submit>|
        Then check list
             |key|value|
             |order|order1|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |operation|submit|type|state|
             |撤销||撤销|编辑中|
             |编辑|提交|撤销|审批中|
             |审批|审批|撤销|审批中|
             |审批|审批|撤销|审批中|
             |审批|审批|撤销|审批中|
             |审批|审批|撤销|审批中|
             |审批|审批|撤销|审批中|
             |审批|审批|撤销|审批中|
             |审批|审批|撤销|已生成|
