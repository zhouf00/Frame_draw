import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from TmpData import _read_data, tmp_file
import pandas as pd

colour = ["r", "g", "b", "y"]
yp_list = ["叶片1", "叶片2", "叶片3"]

class Graph_Func(QWidget):

    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.plt = pg.PlotWidget()
        self.plt.addLegend(size=(150, 80))
        self.plt.showGrid(x=True, y=True, alpha=0.5)
        self.main_layout.addWidget(self.plt)
        self.setLayout(self.main_layout)

    def set_data(self, file_name):
        self.data = pd.DataFrame(pd.read_csv(file_name))

    def plt_show(self, num):
        self.main_layout.removeWidget(self.plt)

        self.plt = pg.PlotWidget()
        self.plt.addLegend(size=(150, 80))
        self.plt.showGrid(x=True, y=True, alpha=0.5)

        for i in num.split(","):
            i = int(i)
            self.plt.plot(x=self.data.index.tolist(), y=list(self.data.iloc[:,i]), pen=colour[i-1],
                     name=yp_list[i-1])

        self.label = pg.TextItem()  # 创建一个文本项
        self.plt.addItem(self.label)
        self.vLine = pg.InfiniteLine(angle=90, movable=False, )
        self.hLine = pg.InfiniteLine(angle=0, movable=False, )
        self.plt.addItem(self.vLine, ignoreBounds=True)  # 在图形部件中添加垂直线条
        self.plt.addItem(self.hLine, ignoreBounds=True)  # 在图形部件中添加水平线条

        self.move_slot = pg.SignalProxy(self.plt.scene().sigMouseMoved,
                                        rateLimit=60, slot=self.mouse_moved)
        self.main_layout.addWidget(self.plt)

    def mouse_moved(self, event=None):

        if event is None:
            print("事件为空")
        else:
            pos = event[0]  ## using signal proxy turns original arguments into a tuple
            try:
                if self.plt.sceneBoundingRect().contains(pos):
                    mousePoint = self.plt.plotItem.vb.mapSceneToView(pos)
                    index = int(mousePoint.x())
                    #print("坐标：", (index, mousePoint.y()), "值：",(self.data.iloc[:, 0][index]))
                    if 0 < index < len(self.data):
                        self.label.setHtml("<p style='color:white'>频率：{0}</p>"
                                           .format(self.data.iloc[:, 0][index].astype(str)))
                        self.label.setPos(mousePoint.x(), mousePoint.y())
                    self.vLine.setPos(mousePoint.x())
                    self.hLine.setPos(mousePoint.y())
            except Exception as e:
                print(e)

if __name__ == '__main__':
    a = Graph_Func()
    a.test(_read_data())
    pass