import pyqtgraph as pg
from TmpData import _read_data

colour = ["r", "g", "b"]
yp_list = ["叶片1", "叶片2", "叶片3"]

class Graph_Func(object):

    def data_to_dict(self, data_list=_read_data()):
        self.mydict = {}
        for my_vars, i in zip(data_list, range(len(data_list))):
            print(my_vars, i)
            tmp_dict = {}
            for var, j in zip(my_vars, range(len(my_vars))):
                tmp_dict[var[0]] =var[1]
            self.mydict[i] = tmp_dict

    def test(self, mlist):
        for var, i in zip(mlist, range(len(mlist))):
            print(var)

    def plt_init(self):
        plt = pg.PlotWidget()
        plt.addLegend(size=(150, 80))
        plt.showGrid(x=True, y=True, alpha=0.5)
        return plt

    def plt_show(self, num):

        plt = pg.PlotWidget()
        plt.addLegend(size=(150, 80))
        plt.showGrid(x=True, y=True, alpha=0.5)
        for i in num.split(","):
            i = int(i)-1
            plt.plot(x=list(self.mydict[i].keys()), y=list(self.mydict[i].values()), pen=colour[i],
                     name=yp_list[i])
        return plt


if __name__ == '__main__':
    a = Graph_Func()
    a.test(_read_data())
    pass