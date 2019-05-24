import wx
from v1图形.wxplot_test1 import Plot_Pnl
from EMD_API import ParaEMD
from random import sample

class TestFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(TestFrame, self).__init__(*args, **kw)
        self.SetSize((800, 650))
        self.SetTitle("测试")

        topvb = wx.BoxSizer(wx.VERTICAL)
        hb = wx.BoxSizer(wx.HORIZONTAL)
        self.wxplot = Plot_Pnl(self)
        self.Pemd = ParaEMD()
        #self.wxplot2 = Plot_Pnl(self)
        self.hb_button1 = wx.Button(self, label=u"测试")

        hb.Add(self.hb_button1, 0, wx.EXPAND | wx.ALL, 5)
        topvb.AddMany([(hb, 0, wx.EXPAND | wx.ALL, 5),
                    (self.wxplot, 1, wx.EXPAND | wx.ALL, 5),
                    #(self.wxplot2, 1, wx.EXPAND | wx.ALL, 5),
                    ])

        self.SetSizer(topvb)

        self.hb_button1.Bind(wx.EVT_BUTTON, self.test1)

        self.Show(True)

    def test1(self, e):
        #self.wxplot._cla()
        self.wxplot._draw_new(self.Pemd.test_numpy(), sample(range(0,3),3))
        pass

if __name__ == '__main__':
    app = wx.App()
    win = TestFrame(None)
    app.MainLoop()