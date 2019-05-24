# 1.面向对象化
# 2.继承类
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow


class Gui_1():

    def __init__(self):
        self._initUI()

    def _initUI(self):
        self.win = QWidget()
        self.win.setWindowTitle("周凡测试GUI")

        self.win.show()


# 继承自QWidget模块
class Gui_2(QWidget):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        self.setWindowTitle("周凡测试GUI（QWidget模块）")
        self.show()


# 继承QMainWindow自模块
class Gui_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        self.setWindowTitle("周凡测试GUI(QMainWindow自模块)")
        self.resize(400, 100)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #gui = Gui_1()
    #gui = Gui_2()
    gui = Gui_3()
    sys.exit(app.exec_())

