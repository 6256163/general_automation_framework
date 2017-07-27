@chrome
Feature: Order
    User can new order and audit order to make it switch to correct type and state.

    Scenario: new CPT order
        Given navigate to page
             |key|value|
             |menu|order_list|
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
        Examples: Prepare order
             |order_num|
             |order1|

    Scenario Outline: audit a pre-order to complete
        Given navigate to page
             |key|value|
             |menu|order_list|
        And an order
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

