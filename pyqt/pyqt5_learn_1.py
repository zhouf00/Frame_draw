import sys
from PyQt5.QtWidgets import *

# 实例化一应用程序对象QApplication()
app = QApplication(sys.argv)
# 创建一个QWidget()对象
win = QWidget()
# 再使用QWidget()对象的show()方法将创建的窗口显示出来
win.show()
# 调用应用程序的exec_()方法来运行程序的主循环，并使用sys.exit()方法确保程序能完美退出
sys.exit(app.exec_())