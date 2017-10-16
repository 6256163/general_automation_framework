@chrome
Feature: order content
  Check the order content can be save and show in page
  Background: Navigate to Order list page
    Given switch system
      |key|value|
      |type|视频|
    Given navigate
      |key|value|
      |菜单|order_list|


  Scenario Outline: Verify pre-order fields can be saved and showed
    When new
    And stock query
      |key|value|
      |广告位|<adr>|
    And add new
      |key|value|
      |排期|<slot>|
      |下单|加入|
    And store order
      |orderno|
      |<order_num>|
    And fill
      |key|value|
      |名称 |<name>|
      |广告主|<adv>|
      |提交|<submit>|
    Then check list
      |key|value|
      |order|<order_num>|
      |订单名称|<name>|
      |广告主|<adv>|
#    When audit <times>
#      |key|value|
#      |order|<order_num>|
#      |operation|<audit>|
#      |提交|<submitA>|
    When operate
      |key|value|
      |order|<order_num>|
      |operation|编辑|
    Then check order content
      |key|value|
      |名称|<name>|
      |广告主|<adv>|
    Examples: order number
      |order_num|submit|adr|slot|name|adv|times|audit|submitA|
      |order1|提交|视频广告.通用位置.通用前贴|0|111订单名称！@#|六间房|2|审批|审批|


