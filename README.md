# 使用手册
## 框架简介
- 通用型自动化测试框架，基于WebDriver，关键字驱动模式CSV。

## Testcase说明
#### 文件类型：CSV
#### 列详细：
- TestCase：测试用例编号，不区分大小写。
- Step：测试用例步骤，数字1、2、3……
- Browser：确定当前测试使用的浏览器类型，目前支持CHROME，FIREFOX。不区分大小写
- Action：行为操作名称，即调用对应的方法名。不区分大小写
- ActionBy：Action参数。元素定位属性。不区分大小写
    * **ID**
    * **NAME**
    * **XPATH**
    * **LINK_TEXT**（LINK TEXT）
    * **TAG_NAME**（TAG NAME）
    * **CSS_SELECTOR**（CSS SELECTOR）
    * **CLASS_NAME**（CLASS NAME）
    * **PARTIAL_LINK_TEXT**（PARTIAL LINK TEXT）
- ActionLocation：Action参数。元素定位参数。不区分大小写
- ActionValue：Action参数。待输入的值。大小写敏感
- Expect：验证操作名称，即调用对应的方法名
- ExpectBy：Expect参数。元素定位属性
    * **ID**
    * **NAME**
    * **XPATH**
    * **LINK_TEXT**（LINK TEXT）
    * **TAG_NAME**（TAG NAME）
    * **CSS_SELECTOR**（CSS SELECTOR）
    * **CLASS_NAME**（CLASS NAME）
    * **PARTIAL_LINK_TEXT**（PARTIAL LINK TEXT）
- ExpectLocation：Expect参数。元素定位参数
- ExpectProperty：Expect参数。元素属性
- ExpectValue：Expect参数。期望值
- PageObject：根据Web定制，非通用调用的模块，即Page类
- PageAction：Page类对应方法名
- PageValue：传入给方法的参数
  
## 关键词及参数说明（Action列）：
- **OPEN_PAGE** 在浏览器打开页面，网址或HTML文件
    - ActionValue：完整的网址连接
    - ActionLocation：HTML文件夹路径

        例：
        <table>
        <tr>
            <th>Action</th>
            <th>ActionBy</th>
            <th>ActionLocation</th>
            <th>ActionValue</th>
        </tr>
        <tr>
            <td>OPEN_PAGE</td>
            <td></td>
            <td>/Path/to/file</td>
            <td>example.html</td>
        </tr>
        <tr>
            <td>OPEN_PAGE</td>
            <td></td>
            <td></td>
            <td>http://baidu.com</td>
        </tr>
        </table>
- **INPUT_VALUE** 针对HTML元素，输入值
    - ActionBy：元素查询方式。
    - ActionLocation：ActionBy对应value
    - ActionValue：需要输入的值

        例：
        <table>
        <tr>
            <th>Action</th>
            <th>ActionBy</th>
            <th>ActionLocation</th>
            <th>ActionValue</th>
        </tr>
        <tr>
            <td>INPUT_VALUE</td>
            <td>XPATH</td>
            <td>//div</td>
            <td>示例</td>
        </tr>
        </table>
    
- **CLICK** 点击HTML元素
    - ActionBy：元素查询方式。
    - ActionLocation：ActionBy对应value
    - ActionValue：需要输入的值

        例：
        <table>
        <tr>
            <th>Action</th>
            <th>ActionBy</th>
            <th>ActionLocation</th>
            <th>ActionValue</th>
        </tr>
        <tr>
            <td>CLICK</td>
            <td>XPATH</td>
            <td>//div</td>
            <td></td>
        </tr>
        </table>

- **SWITCH_WINDOW** 窗口切换
    - ActionValue：目标窗口的title值

        例：
        <table>
        <tr>
            <th>Action</th>
            <th>ActionBy</th>
            <th>ActionLocation</th>
            <th>ActionValue</th>
        </tr>
        <tr>
            <td>SWITCH_WINDOW</td>
            <td></td>
            <td></td>
            <td>test_百度搜索</td>
        </tr>
        </table>
        
- **SWITCH_FRAME** iframe切换
    - ActionBy：元素查询方式。为空时默认用ID或NAME搜索。仅针对SWITCH_FRAME适用
    - ActionLocation：ActionBy对应value

        例：
        <table>
        <tr>
            <th>Action</th>
            <th>ActionBy</th>
            <th>ActionLocation</th>
            <th>ActionValue</th>
        </tr>
        <tr>
            <td>SWITCH_FRAME</td>
            <td>XPATH</td>
            <td>//div</td>
            <td></td>
        </tr>
        <tr>
            <td>SWITCH_FRAME</td>
            <td></td>
            <td>ElementID</td>
            <td></td>
        </tr>
        </table>
        
- **SWITCH_PARENT_FRMAE** 返回上级iframe

- **SWITCH_DEFAULT_CONTENT** 返回windows


## 关键词及参数说明（Expect列）：
- **VERIFY** 验证属性值与期望结果
    - ExpectBy：元素查询方式。
    - ExpectLocation：ExpectBy对应value
    - ExpectProperty：需要验证的元素属性
    - ExpectValue：需要输入的值

        例：
        <table>
        <tr>
            <th>Expect</th>
            <th>ExpectBy</th>
            <th>ExpectLocation</th>
            <th>ExpectProperty</th>
            <th>ExpectValue</th>
        </tr>
        <tr>
            <td>VERIFY</td>
            <td>XPATH</td>
            <td>//div</td>
            <td>text</td>
            <td>比对文本属性</td>
        </tr>
        </table>
- **COMPARE** 比较多个元素的属性值
    - ExpectBy：元素查询方式。同VERIFY，多个参数之间用分号（;）隔开
    - ExpectLocation：ExpectBy对应value。同VERIFY，多个参数之间用分号（;）隔开
    - ExpectProperty：需要验证的元素属性。同VERIFY，多个参数之间用分号（;）隔开

        例：
        <table>
        <tr>
            <th>Expect</th>
            <th>ExpectBy</th>
            <th>ExpectLocation</th>
            <th>ExpectProperty</th>
            <th>ExpectValue</th>
        </tr>
        <tr>
            <td>COMPARE</td>
            <td>XPATH;ID</td>
            <td>//div;element_id</td>
            <td>text;value</td>
            <td></td>
        </tr>
        </table>
        
