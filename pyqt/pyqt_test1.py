import pyqtgraph as pg
import tushare as ts
import numpy as np

data = ts.get_hist_data("sh", start="2018-4-20", end="2019-5-20").sort_index()

xdict = dict(enumerate(data.index))

axis_1 = [(i, list(data.index)[i]) for i in range(0, len(data.index),5)]


# 首先实例化一个QT实例：
app = pg.QtGui.QApplication([])

# 接着借助GraphicsWindow()子模块创建一个空的图形窗口，并使用title参数设置了窗口的标题：
win = pg.GraphicsWindow(title="测试QT")

# 通过之前创建的字典xdict和列表axis_1，设置图形的X坐标轴刻度文本，orientation参数表示坐标轴的位置：
stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks([axis_1,xdict.items()])

# 在窗口中添加一个空的图形，通过axisItems参数指定坐标轴及其内容，并使用title参数设置了图形的标题：
plot = win.addPlot(axisItems={'bottom': stringaxis}, title='上证指数 - zmister.com绘制')

# 在图形中添加一个文本：
label = pg.TextItem()
plot.addItem(label)

# 设置图形的图例：
plot.addLegend(size=(150,80))

# 设置图形网格的形式，我们设置显示横线和竖线，并且透明度惟0.5：
plot.showGrid(x=True, y=True, alpha=0.5)

# 绘制开盘和收盘的指数，pen参数表示线的颜色，name参数可用于图例的显示，symbolBrush用来设置点的颜色：
plot.plot(x=list(xdict.keys()), y=data['open'].values, pen='r', name='开盘指数',symbolBrush=(255,0,0),)
plot.plot(x=list(xdict.keys()), y=data['close'].values, pen='g', name='收盘指数',symbolBrush=(0,255,0))

# 设置图形的轴标签：
plot.setLabel(axis='left',text='指数')
plot.setLabel(axis='bottom',text='日期')

# 最后设置十字光标：
vLine = pg.InfiniteLine(angle=90, movable=False, )
hLine = pg.InfiniteLine(angle=0, movable=False, )
plot.addItem(vLine, ignoreBounds=True)
plot.addItem(hLine, ignoreBounds=True)
vb = plot.vb
def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if plot.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        pos_y = int(mousePoint.y())
        print(index)
        if 0 < index < len(data.index):
            print(xdict[index], data['open'][index], data['close'][index])
            label.setHtml(
                "<p style='color:white'>日期：{0}</p><p style='color:white'>开盘：{1}</p><p style='color:white'>收盘：{2}</p>".format(
                    xdict[index], data['open'][index], data['close'][index]))
            label.setPos(mousePoint.x(), mousePoint.y())
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())

proxy = pg.SignalProxy(plot.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

# 再按常例，调用app的exec_()方法即可：
app.exec_()