## 环境配置

1. 虚拟环境

```shell
virtualenv venv
```

3. 下载相关的文件包

```shell
# pyside6
pip install PySide6 -i https://pypi.douban.com/simple/

# sklearn
pip install -U scikit-learn
```

## 教程地址

- [Python Qt 教程 | 白月黑羽](https://www.byhy.net/tut/py/gui/qt_01/)
- [pythongui tutorials](https://www.pythonguis.com/tutorials/)

## 笔记

1. `.ui` 文件的使用方法

```shell
pyside6-uic  input.ui > output.py
```

2. `.qrc` 文件使用方法

```shell
pyside6-rcc input.qrc > output.py
```

## 写代码

1. 通过 setParent 可以设置嵌套关系
2. Widget 可以设置 animation
3. 定义 childXLayout = xxxLayout(parentX),与定义 parentX.setLayout(childXLayout) 有点区别