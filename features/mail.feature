# Created by tianzhang at 2017/9/22
@chrome
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Create special order
      When store mail id
          |mailid|
          |mail1|
      And logout
      And login
          |key|value|
          |username|14041352|
          |password|123456|
          |verifycode|imqa|
      And navigate
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
          |特批|1|
          |名称 |111|
          |广告主|六间房|
          |提交|提交|
      Then check mail
          |key|value|
          |mailid|mail1|
          |发送|jiaming_wu@quantone.com|
          |抄送|17032762@cnsuning.com|
          |主题|【特批】请审批询量单;order1|



  Scenario Outline: audit special order
      When store mail id
          |mailid|
          |mail1|
      And logout
      And login
          |key|value|
          |username|<用户>|
          |password|123456|
          |verifycode|imqa|
      And navigate
          |key|value|
          |菜单|order_list|
      And operate
          |key|value|
          |order|order1|
          |operation|<操作>|
      And fill
          |key|value|
          |金额|<金额>|
          |成本|<成本>|
          |预计支付|<预计支付>|
          |AE|<AE>|
          |询量组负责人|<next>|
          |配合销售|<配合销售>|
          |提交|<提交>|
      Then check mail
          |key|value|
          |mailid|mail1|
          |发送|<发送>|
          |抄送|<抄送>|
          |主题|<主题>|

      Examples:
          |用户|操作|提交|AE|金额|成本|预计支付|next|配合销售|发送|抄送|主题|
          |14040290|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com|【特批】请审批询量单;order1|
          |14042449|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com|【特批】请审批询量单;order1|
          |15010324|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com|【特批】请审批询量单;order1|
          |15100637|审批|审批|||||||17032762@cnsuning.com|None|询量单;order1;已审批通过，请尽快下单|
          |14041352|编辑|提交|邮件AE|||2||邮件配合销售|jiaming_wu@quantone.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;AE审核|
          |15010387|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;商务审核|
          |15010279|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;财务审核|
          |15050340|审批|审批|||||||wujmd@cnsuning.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;审核通过，执行人员请执行|

  Scenario: Create client order
      When store mail id
          |mailid|
          |mail1|
      And logout
      And login
          |key|value|
          |username|14041352|
          |password|123456|
          |verifycode|imqa|
      And navigate
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
          |提交|提交|
      Then check mail
          |key|value|
          |mailid|mail1|
          |发送|jiaming_wu@quantone.com|
          |抄送|17032762@cnsuning.com|
          |主题|请审批询量单;order1|

  Scenario Outline: audit client order
      When store mail id
          |mailid|
          |mail1|
      And logout
      And login
          |key|value|
          |username|<用户>|
          |password|123456|
          |verifycode|imqa|
      And navigate
          |key|value|
          |菜单|order_list|
      And operate
          |key|value|
          |order|order1|
          |operation|<操作>|
      And fill
          |key|value|
          |金额|<金额>|
          |成本|<成本>|
          |预计支付|<预计支付>|
          |AE|<AE>|
          |询量组负责人|<next>|
          |配合销售|<配合销售>|
          |提交|<提交>|
      Then check mail
          |key|value|
          |mailid|mail1|
          |发送|<发送>|
          |抄送|<抄送>|
          |主题|<主题>|

      Examples:
          |用户|操作|提交|AE|金额|成本|预计支付|next|配合销售|发送|抄送|主题|
          |15010312|审批|审批|||||yes||jiaming_wu@quantone.com|17032762@cnsuning.com|请审批询量单;order1|
          |15010370|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com|请审批询量单;order1|
          |14040290|审批|审批|||||||17032762@cnsuning.com|None|询量单;order1;已审批通过，请尽快下单|
          |14041352|编辑|提交|邮件AE|||2||邮件配合销售|jiaming_wu@quantone.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;AE审核|
          |15010387|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;商务审核|
          |15010279|审批|审批|||||||jiaming_wu@quantone.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;财务审核|
          |15050340|审批|审批|||||||wujmd@cnsuning.com|17032762@cnsuning.com;402005221@qq.com|订单;order1;审核通过，执行人员请执行|

