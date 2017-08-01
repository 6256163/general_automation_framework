@chrome @skip
Feature: Order
    User can new order and audit order to make it switch to correct type and state.
    Scenario Outline: Create a new order
        When click new order
         And stock query
             |key|value|
             |type|CPT|
             |date|2017-10-13;2017-10-16|
             |0|视频广告.通用位置.通用前贴|
         And select slot and create new order
             |key|value|
             |mode|下单|
             |index|1;2;3|
         And fill and submit info
             |key|value|
             |adv|六间房|
             |submit|提交|
        Then check the order info from order list
             |key|value|
             |类型|询量|
             |状态|审批中|
        And storage order number
             |order_in_storage|
             |<order_num>          |
        Examples: order number
             |order_num|
             |order1   |
             |order2   |
             |order3   |


    Scenario Outline: audit a pre-order to complete
        Given search an order
             |order_in_storage|
             |order1          |
        When audit the order
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |operation|<operation>|
             |submit|<submit>|
        Then check the order info from order list
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
        Given search an order
             |order_in_storage|
             |order2       |
        When audit the order
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |operation|<operation>|
             |submit|<submit>|
        Then check the order info from order list
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
        Given search an order
             |order_in_storage|
             |order3          |
        When audit the order
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |operation|<operation>|
             |submit|<submit>|
        Then check the order info from order list
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
        Given search an order
             |order_in_storage|
             |order2        |
        When audit the order
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |adjust  |<adjust>  |
             |operation|<operation>|
             |submit|<submit>|
        Then check the order info from order list
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
        Given search an order
             |order_in_storage|
             |order1         |
        When audit the order
             |key|value|
             |amount|<amount>|
             |cost|<cost>|
             |pay_date|<pay_date>|
             |adjust  |<adjust>  |
             |operation|<operation>|
             |submit|<submit>|
        Then check the order info from order list
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
        Given search an order
             |order_in_storage|
             |order1         |
        When audit the order
             |key|value|
             |operation|<operation>|
             |submit|<submit>|
        Then check the order info from order list
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
