# 添加状态栏 菜单栏 退出按键
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


# 继承QMainWindow自模块
class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        self.setWindowTitle("周凡测试GUI(QMainWindow自模块)")
        self.resize(400, 300)
        # 设置状态消息栏文本
        self.statusBar().showMessage("文本状态栏")

        # 创建一个菜单栏
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


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()

    sys.exit(app.exec_())

