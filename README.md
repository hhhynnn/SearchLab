通过 main.py 运行

spider.py 是爬BBC的脚本, 使用了 localhost:10808 端口的代理

## 依赖

```shell
pip install pyside2 -i https://pypi.douban.com/simple/
pip install -U scikit-learn
pip install requests
pip install lxml
pip install pysocks
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
