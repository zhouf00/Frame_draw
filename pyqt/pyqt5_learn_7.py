# 添加Label标签部件
# 添加按钮部件
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import Qt


# 继承QMainWindow自模块
class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

        self.show()

    def _initUI(self):
        self.setWindowTitle("周凡测试GUI(QMainWindow自模块)")
        self.resize(400, 300)
        self.add_menu_and_statu()
        self.grid_layout()

    # 添加菜单栏和状态栏
    def add_menu_and_statu(self):
        self.statusBar().showMessage("文本状态栏")
        #　创建一个菜单栏
        menu = self.menuBar()
        # 创建两个菜单
        file_menu = menu.addMenu("文件")
        file_menu.addSeparator()
        edit_menu = menu.addMenu("修改")

        # 创建一个行为
        new_action = QAction("新文件", self)
        # 更新状态栏文本
        new_action.setStatusTip("新的文件")
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        # 创建退出行为
        exit_action = QAction("退出", self)
        # 退出操作
        exit_action.setStatusTip("点击退出应用程序")
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut("Ctrl+Q")
        # 添加退出行为菜单上
        file_menu.addAction(exit_action)

    # 添加布局部件
    def grid_layout(self):
        # 两个标签
        label_1 = QLabel("第一个标签", self)
        label_2 = QLabel("第二个标签", self)

        # 两个按钮
        button_1 = QPushButton("按钮1", self)
        button_2 = QPushButton("按钮2", self)
        button_3 = QPushButton("按钮3", self)

        # 创建一个风格布局对象
        grid_layout = QGridLayout()

        # 在风格中添加窗口部件
        grid_layout.addWidget(label_1, 0, 0)
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(label_2, 1, 0)
        grid_layout.addWidget(button_2, 1, 1)

        grid_layout.addWidget(button_3, 2, 0, 1, 5)
        #　对齐方式
        grid_layout.setAlignment(Qt.AlignTop)
        grid_layout.setAlignment(label_1, Qt.AlignRight)

        # 创建一个窗口对象
        layout_widget = QWidget()

        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()

    sys.exit(app.exec_())

