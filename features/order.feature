@tags @tag
Feature: Order
    User can new order and audit order to make it switch to correct type and state.

    Background: Launch browser
        Given browser should be launched
            |browser|
            |chrome |
        And login page is opened
        When input user login info and submit
             |key|value|
             |username|2|
             |password|123456|
             |verifycode|imqa|
        Then show the index page


    Scenario: new CPT order
        Given navigate to page
             |key|value|
             |menu|order_list|
        When click new order
         And stock query
             |key|value|
             |type|CPT|
             |date|2017-10-13;2017-10-16|
             |0|网站页面广告.首页.网站首页通栏4|
         And select slot and create new order
             |key|value|
             |mode|下单|
             |index|1;2;3|
         And fill and submit info
             |key|value|
             |adv|六间房|
             |operation|提交|
        Then check the order info from order list
             |key|value|
             |类型|询量|
             |状态|审批中|
         And storage order number
             |order_in_storage|
             |order1          |

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
        Then check the order info from order list
             |key|value|
             |类型|<type>|
             |状态|<state>|
        Examples: Per-order
             |amount|cost|pay_date|operation|type|state|
             ||||审批|询量|审批中|
             ||||审批|新设|待下单|
             |100|200|2|编辑|新设|审批中|
             ||||审批|新设|审批中|
             ||||审批|新设|审批中|
             ||||审批|新设|已生成|
