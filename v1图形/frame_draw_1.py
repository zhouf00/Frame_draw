import wx
from wx import adv
from wx.lib import plot
from Matplotlib_test1 import *
from v1图形.test_data import *


class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.SetSize((700, 450))
        self.SetTitle("风机采集图形化")

        # 面板设计
        self._init_frame()

        # 事件绑定
        self._func_event()

        self.Center()
        self.Show()

    def _init_frame(self):
        # 设置面板各个功能
        pnl = wx.Panel(self)
        vb = wx.BoxSizer(wx.VERTICAL)
        hb1 = wx.BoxSizer(wx.HORIZONTAL)
        hb2 = wx.BoxSizer(wx.HORIZONTAL)
        hb2_v1 = wx.BoxSizer(wx.VERTICAL)
        hb2_h2 = wx.BoxSizer(wx.HORIZONTAL)

        ######################################
        # 第一层 配置文件
        ######################################
        text1 = wx.StaticText(pnl, wx.ID_ANY, u"风场")
        self.hb1_listc2 = wx.Choice(pnl, choices=wind_field)
        self.hb1_listc2.SetSelection(0)
        text3 = wx.StaticText(pnl, wx.ID_ANY, u"风机")
        self.hb1_textc4 = wx.TextCtrl(pnl)
        text5 = wx.StaticText(pnl, wx.ID_ANY, u"叶片ID")
        self.hb1_listc6 = wx.Choice(pnl, choices=wind_blade)
        self.hb1_listc6.SetSelection(0)
        text7 = wx.StaticText(pnl, wx.ID_ANY, u"信号类型")
        self.hb1_listc8 = wx.Choice(pnl, choices=signal_type)
        self.hb1_listc8.    SetSelection(0)
        text9 = wx.StaticText(pnl, wx.ID_ANY, u"时间")
        self.hb1_time10 = adv.DatePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                            wx.DefaultPosition, wx.DefaultSize, adv.DP_DEFAULT)

        hb1.AddMany([(text1,  0, wx.ALIGN_CENTER | wx.ALL, 10),
                     (self.hb1_listc2, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text3, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_textc4, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text5, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_listc6, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text7, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_listc8, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text9, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_time10, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     ])

        ######################################
        # 第二层左侧 配置文件
        ######################################

        fl_list = ["IMF1", "IMF2", "IMF3"]
        self.hb2_v_box1 = wx.RadioBox(pnl, label=u"IMF分量",
                                        choices=fl_list, majorDimension = 3, style = wx.RA_SPECIFY_ROWS)
        data_list = ["叶片1", "叶片2", "叶片3"]
        self.hb2_v_box2 = wx.RadioBox(pnl, label=u"显示优先级",
                                      choices=data_list, majorDimension=3, style=wx.RA_SPECIFY_ROWS)
        self.hb2_v_button1 = wx.Button(pnl, label=u"运行")
        hb2_v1.AddMany([(self.hb2_v_box1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (self.hb2_v_box2, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (self.hb2_v_button1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           ])
        # self.hb2__box1.GetStringSelection()  # 获取单选的值
        ######################################
        # 第二层右侧 配置文件
        ######################################
        hb2_v_draw = plot.PlotCanvas(pnl)
        gc = self.test_draw(hb2_v_draw)
        hb2_v_draw.Draw(gc)
        hb2_h2.Add(hb2_v_draw, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        ######################################
        # 所有面板汇合
        ######################################
        h1_line = wx.StaticLine(pnl, wx.ID_ANY)
        h2_line = wx.StaticLine(pnl,wx.ID_ANY, style=wx.LI_VERTICAL)
        hb2.AddMany([(hb2_v1, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                     (h2_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                     (hb2_h2, 3, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),])
        vb.AddMany([(hb1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (h1_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (hb2, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    ])
        pnl.SetSizer(vb)
        self.CreateStatusBar()

    def _func_event(self):
        pass

    def test_draw(self, draw1):
        data = [[1, 10], [2, 5], [3, 10], [4, 5]]
        line = plot.PolyLine(data, colour="red", width=1)
        data2 = [[1, 12], [2, 9], [3, 20], [4, 5]]
        line2 = plot.PolyLine(data2, colour="green", width=1)
        gc = plot.PlotGraphics([line, line2], "test", "x", "y")
        return gc

if __name__ == '__main__':
    app = wx.App()
    win = MyFrame(None)
    app.MainLoop()