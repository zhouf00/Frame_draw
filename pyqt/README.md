# PYQT5 学习

图形化实例

## 创建第一个程序

[pyqt5_learn_1.py]()

[pyqt5_learn_2.py]()


## 程序面向对象化及继承

[pyqt5_learn_3.py]()


## 添加状态栏 菜单栏 退出按键

[pyqt5_learn_4.py]()

## 添加Label标签部件，添加按钮部件

[pyqt5_learn_5.py]()

## 使用水平垂直布局

[pyqt5_learn_6.py]()

## 使用网格布局

我们从PyQt5的QtCore模块中导入了Qt模块，用来指定对齐方式，使用setAlignment来指定这个表格而已的对齐方式

	from PyQt5.QtCore import Qt 
	grid_layout.setAlignment(Qt.AlignTop)

[pyqt5_learn_7.py]()

## ui文件转Python文件

	pyuic5 -o complex.py conplex.ui
