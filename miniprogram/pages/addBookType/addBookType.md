# addBookType 页面功能文档

## 页面功能

`addBookType` 页面用于添加新的账单类别或计划。用户可以选择图标、输入类别名称、设置计划金额（如果是添加计划），并提交保存。

## 关键功能

### 1. 初始化页面

- 根据传入参数设置页面类型（添加类别或计划）和账单类型（支出或收入）。
- 设置页面标题为“添加支出类别”或“添加收入计划”等。

### 2. 选择图标

- 用户可以从图标列表中选择一个图标，选中的图标会高亮显示。

### 3. 输入类别名称

- 用户可以输入类别或计划的名称，限制最大长度为 6 个字符。

### 4. 输入计划金额

- 如果是添加计划，用户需要输入计划金额，金额不能为 0。

### 5. 提交新增

- 验证输入内容的有效性后，调用相应的云函数 `addBookType` 或 `addPlanList` 将新类别或计划保存到数据库。

