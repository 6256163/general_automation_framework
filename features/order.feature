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
        Given navigate to order_list page
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

    Scenario: audit a new order to complete
        Given a new order is saved
          """
          Given navigate to order_list page
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
             |operation|保存|
          Then check the order info from order list
             |key|value|
             |类型|询量|
             |状态|编辑中|
          """
        When audit the order <times> times
        Then check the order info from order list
             |key|value|
             |类型|新设|
             |状态|待提交|