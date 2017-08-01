@chrome
Feature: Price
    User can new price and audit price to make it switch to correct type and state.
    Scenario Outline: Create a new price
        When new a price
        And fill and submit price form
            |key|value|
            |adv|六间房  |
            |from|3   |
            |to  |5|
            |adr |视频广告.通用位置.通用前贴;视频广告.通用位置.通用暂停|
            |area|中国.江苏.南京;中国.浙江      |
            |port|客户端.Ipad;客户端.Ipad      |
            |price|500/1000;5/10          |
            |type |硬广;贴片           |
            |submit|保存并提交审批     |



        Examples: price
            |aaa|
            |111|