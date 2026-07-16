# Qt 开发指南

## 环境配置

### 安装 Qt
1. 下载 Qt 安装器
2. 选择 Qt 6.11.1 版本
3. 安装 MinGW 编译器

### 创建项目
```bash
# 使用 Qt Creator 创建项目
# 或者使用 CMake
cmake -S . -B build
cmake --build build
```

## 核心概念

### 信号与槽
```cpp
connect(sender, &Sender::signal, receiver, &Receiver::slot);
```

### Widget 布局
- QVBoxLayout - 垂直布局
- QHBoxLayout - 水平布局
- QGridLayout - 网格布局

### 事件处理
```cpp
void mousePressEvent(QMouseEvent *event) override;
void keyPressEvent(QKeyEvent *event) override;
```

## 常用组件

| 组件 | 用途 |
|------|------|
| QPushButton | 按钮 |
| QLabel | 标签 |
| QLineEdit | 单行输入框 |
| QTextEdit | 多行输入框 |
| QListWidget | 列表 |
| QTreeWidget | 树形结构 |

## 📚 学习资源

- Qt 官方文档：https://doc.qt.io
- Qt 示例代码：Qt Creator 内置
