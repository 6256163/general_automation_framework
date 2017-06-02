# 使用手册
## 框架简介
- 通用型自动化测试框架，基于WebDriver，关键字驱动模式CSV。PageObject为订制，非通用。

## Testcase说明
1. 文件类型：CSV
2. 列详细：
    1. TestCase：测试用例编号，不区分大小写。
    2. Step：测试用例步骤，数字1、2、3……
    3. Browser：确定当前测试使用的浏览器类型，目前支持CHROME，FIREFOX。不区分大小写
    4. Action：行为操作名称，即调用对应的方法名。不区分大小写[详细说明]
    5. ActionBy：Action参数。元素定位属性。不区分大小写[详细说明]
    6. ActionLocation：Action参数。元素定位参数。不区分大小写
    7. ActionValue：Action参数。待输入的值。大小写敏感
    8. Expect：验证操作名称，即调用对应的方法名
    9. ExpectBy：Expect参数。元素定位属性
    10. ExpectLocation：Expect参数。元素定位参数
    11. ExpectProperty：Expect参数。元素属性
    12. ExpectValue：Expect参数。期望值
    13. PageObject：调用的模块，即Page类
    14. PageAction：Page类对应方法名
    15. PageValue：传入给方法的参数
  
3. 关键词说明（Action列）：
    ##### open_page
    * ActionValue：完整的网址连接，例http://baidu.com。或HTML文件名配合ActionLocation定位文件路径
    * ActionLocation：HTML文件夹路径。例 /file/path/
    ##### input_value
    * ActionBy：
