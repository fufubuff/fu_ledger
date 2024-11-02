# bookTypeList 页面功能文档

## 页面功能
`bookTypeList` 页面用于展示账单类别列表，支持查看、删除类别以及切换账单类型（支出或收入）。

## 关键功能

### 1. 初始化页面
- 页面加载时，根据传入参数设置账单类型（支出或收入）。

### 2. 显示账单类别列表
- 页面显示时，通过调用云函数 `getBookType` 获取当前账单类型的类别列表，并更新页面数据。

### 3. 显示和隐藏删除按钮
- 用户可以点击类别项，显示相应的删除按钮。
- 点击其他地方时，删除按钮会自动隐藏。

### 4. 删除账单类别
- 用户可以点击删除按钮删除特定类别。
- 若尝试删除公用类别，系统会弹出提示信息，禁止删除操作。
- 删除成功后，更新类别列表。

### 5. 切换账单类型
- 用户可以选择支出或收入类型，页面会更新类别列表以显示相应的类别。

### 6. 添加新账单类别
- 用户可以点击添加按钮，跳转到 `addBookType` 页面，添加新的账单类别。