# 画图类
import wx
from wx import Panel as wxpnl
from wx.lib import plot


class Plot_Pnl(wxpnl):

    colour_list = ["red", "green", "blue", "yellow", "pink"]

    def __init__(self, *args, **kw):
        super(Plot_Pnl, self).__init__(*args, **kw)
        self.my_cas = plot.PlotCanvas(self)
        vb = wx.BoxSizer(wx.VERTICAL)
        hb = wx.BoxSizer(wx.HORIZONTAL)
        line = plot.PolyLine([])
        self.gc = plot.PlotGraphics([line], u"测试波形图", "x", "y")
        self.my_cas.Draw(self.gc)
        vb.AddMany([(hb, 0, wx.EXPAND | wx.ALL, 5),
                    (self.my_cas, 1, wx.EXPAND | wx.ALL, 0),
                    ])
        self.SetSizer(vb)

    def _Updataplot(self, gc):
        self.my_cas.Draw(gc)

    def _cla(self):
        self.my_cas.Clear()

    def _draw_new(self, args, num):
        tmp_data = []
        res_list = []
        for i in range(len(args)):
            tmp_data.append(plot.PolyLine(args[i], colour=self.colour_list[i], width=1, legend="abc"))
        for i in range(len(tmp_data)):
            res_list.append(tmp_data[num[i]])
        gc = plot.PlotGraphics(res_list, u"新图", "x", "y")
        self._Updataplot(gc)

    def _draw_new_one(self, args):
        tmp_data = []
        tmp_data.append(plot.PolyLine(args, colour="pink", width=1))
        gc = plot.PlotGraphics(tmp_data, u"新图", "x", "y")
        self._Updataplot(gc)



