# Created by tianzhang at 2017/9/21
@chrome
Feature: Order audit graph
  # Enter feature description here
  Scenario: create order
      Given switch system
          |key|value|
          |type|体育|
      When navigate
          |key|value|
          |菜单|order_list|
      And new
      And stock query
          |key|value|
          |广告位|视频广告.通用位置.通用前贴|
      And add new
          |key|value|
          |排期|1|
          |下单|加入|
          |投放量|5|
      And store order
          |orderno|
          |order1|
      And fill
          |key|value|
          |名称 |111|
          |广告主|六间房|
          |提交|保存|

  Scenario Outline: audit graph
      Given navigate
          |key|value|
          |菜单|order_audit|
      And store audit graph
          |key|value|
          |阶段|<阶段1>|
          |状态|<状态1>|
          |key|<阶段1>-<状态1>|
      And store audit graph
          |key|value|
          |阶段|<阶段2>|
          |状态|<状态2>|
          |key|<阶段2>-<状态2>|
      When navigate
          |key|value|
          |菜单|order_list|
      When operate
          |key|value|
          |order|order1|
          |operation|<操作>|
      And fill
          |key|value|
          |金额|<金额>|
          |成本|<成本>|
          |预计支付|<预计支付>|
          |提交|<提交>|
      And navigate
          |key|value|
          |菜单|order_audit|
      Then check audit graph
          |key|value|
          |阶段|<阶段2>|
          |状态|<状态2>|
          |key|<阶段2>-<状态2>;1|
      Then check audit graph
          |key|value|
          |阶段|<阶段1>|
          |状态|<状态1>|
          |key|<阶段1>-<状态1>;-1|
      Examples:
          |阶段1|状态1|阶段2|状态2|操作|提交|金额|成本|预计支付|
          |草稿|待提交|询量组审批|待审核|编辑|提交||||
          |询量组审批|待审核|销售总监审批|待审核|审批|审批||||
          |销售总监审批|待审核|待下单|待下单|审批|审批||||
          |待下单|待下单|AE审批|待审核|编辑|提交|||2|
          |AE审批|待审核|商务审批|待审核|审批|审批||||
          |商务审批|待审核|财务审批|待审核|审批|审批||||
          |财务审批|待审核|结束/关闭|待关联素材|审批|审批||||



  Scenario: Create order
      Given switch system
          |key|value|
          |type|视频|
      When navigate
          |key|value|
          |菜单|order_list|
      And new
      And stock query
          |key|value|
          |广告位|视频广告.通用位置.通用前贴|
      And add new
          |key|value|
          |排期|1|
          |下单|加入|
      And store order
          |orderno|
          |order1|
      And fill
          |key|value|
          |名称 |111|
          |广告主|六间房|
          |提交|保存|

  Scenario Outline: audit graph
      Given navigate
          |key|value|
          |菜单|order_audit|
      And store audit graph
          |key|value|
          |阶段|<阶段1>|
          |状态|<状态1>|
          |key|<阶段1>-<状态1>|
      And store audit graph
          |key|value|
          |阶段|<阶段2>|
          |状态|<状态2>|
          |key|<阶段2>-<状态2>|
      When navigate
          |key|value|
          |菜单|order_list|
      When operate
          |key|value|
          |order|order1|
          |operation|<操作>|
      And fill
          |key|value|
          |金额|<金额>|
          |成本|<成本>|
          |预计支付|<预计支付>|
          |提交|<提交>|
      And navigate
          |key|value|
          |菜单|order_audit|
      Then check audit graph
          |key|value|
          |阶段|<阶段2>|
          |状态|<状态2>|
          |key|<阶段2>-<状态2>;1|
      Then check audit graph
          |key|value|
          |阶段|<阶段1>|
          |状态|<状态1>|
          |key|<阶段1>-<状态1>;-1|
      Examples:
          |阶段1|状态1|阶段2|状态2|操作|提交|金额|成本|预计支付|
          |草稿|待提交|询量组审批|待审核|编辑|提交||||
          |询量组审批|待审核|销售总监审批|待审核|审批|审批||||
          |销售总监审批|待审核|待下单|待下单|审批|审批||||
          |待下单|待下单|AE审批|待审核|编辑|提交|||2|
          |AE审批|待审核|商务审批|待审核|审批|审批||||
          |商务审批|待审核|财务审批|待审核|审批|审批||||
          |财务审批|待审核|结束/关闭|待关联素材|审批|审批||||





