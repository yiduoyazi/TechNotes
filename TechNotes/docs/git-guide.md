# Git 使用指南

## 基础命令

### 初始化仓库
```bash
git init
```

### 添加文件
```bash
git add .
git add filename.txt
```

### 提交更改
```bash
git commit -m "commit message"
```

## 分支管理

### 创建分支
```bash
git branch feature-name
git checkout feature-name
# 或者一步完成
git checkout -b feature-name
```

## 📌 重要提示（master版本）

- 本指南适用于团队协作开发
- 建议使用 Git Flow 工作流
- 定期进行代码审查
- 保持提交历史清晰
