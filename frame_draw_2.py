import wx
from threading import Thread
from wx import adv
from wx.lib import plot
from Matplotlib_test2 import *
from test_data import *


class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.SetSize((800, 500))
        self.SetTitle("风机采集图形化v1")

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
        hb3 = wx.BoxSizer(wx.HORIZONTAL)
        hb3_v1 = wx.BoxSizer(wx.VERTICAL)
        hb3_h2 = wx.BoxSizer(wx.HORIZONTAL)

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

        hb1.AddMany([(text1,  0, wx.ALIGN_CENTER | wx.ALL, 10),
                     (self.hb1_listc2, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text3, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_textc4, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text5, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_listc6, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text7, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_listc8, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     ])

        ######################################
        # 第二层左侧 时间
        ######################################
        text9 = wx.StaticText(pnl, wx.ID_ANY, u"起始:")
        self.hb2_time10 = adv.DatePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                            wx.DefaultPosition, wx.DefaultSize, adv.DP_DEFAULT)
        self.hb2_time11 = adv.TimePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                                    wx.DefaultPosition, (53, 25), adv.DP_DEFAULT)
        text12 = wx.StaticText(pnl, wx.ID_ANY, u"结束：")
        self.hb2_time13 = adv.DatePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                                    wx.DefaultPosition, wx.DefaultSize, adv.DP_DEFAULT)
        self.hb2_time14 = adv.TimePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                             wx.DefaultPosition, (53, 25), adv.DP_DEFAULT)
        self.hb2_button15 = wx.Button(pnl, label=u"运行")

        hb2.AddMany([(text9, 0, wx.ALIGN_CENTER | wx.ALL, 10),
                     (self.hb2_time10, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb2_time11, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text12, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb2_time13, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb2_time14, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb2_button15, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                                          ])

        ######################################
        # 第三层左侧 配置文件
        ######################################

        fl_list = ["IMF1", "IMF2", "IMF3"]
        self.hb3_v_box1 = wx.RadioBox(pnl, label=u"IMF分量",
                                        choices=fl_list, majorDimension = 3, style = wx.RA_SPECIFY_ROWS)
        data_list = ["叶片1", "叶片2", "叶片3"]
        self.hb3_v_box2 = wx.RadioBox(pnl, label=u"显示优先级",
                                      choices=data_list, majorDimension=3, style=wx.RA_SPECIFY_ROWS)
        self.hb3_v_button1 = wx.Button(pnl, label=u"运行")
        hb3_v1.AddMany([(self.hb3_v_box1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (self.hb3_v_box2, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (self.hb3_v_button1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           ])
        # self.hb3__box1.GetStringSelection()  # 获取单选的值
        ######################################
        # 第三层右侧 配置文件
        ######################################
        hb3_v_draw = self.test_draw(pnl)

        hb3_h2.Add(hb3_v_draw, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        ######################################
        # 所有面板汇合
        ######################################
        h1_line = wx.StaticLine(pnl, wx.ID_ANY)
        h2_line = wx.StaticLine(pnl,wx.ID_ANY, style=wx.LI_VERTICAL)
        hb3.AddMany([(hb3_v1, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                     (h2_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                     (hb3_h2, 3, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),])
        vb.AddMany([(hb1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (hb2, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (h1_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (hb3, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    ])
        pnl.SetSizer(vb)
        self.CreateStatusBar()

    def _func_event(self):
        self.Bind(wx.EVT_MOVE, self.on_move)
        self.hb2_button15.Bind(wx.EVT_BUTTON, self._start_event)

    def _start_event(self, e):
        a = self.hb1_listc2.GetStringSelection()
        b = self.hb1_textc4.GetValue()
        c = self.hb1_listc6.GetStringSelection()
        d = self.hb1_listc8.GetStringSelection()
        e = self.hb2_time10.GetValue()
        print(a,b, c, d)
        print(e)

    def _start_func(self):
        pass

    def test_draw(self, pnl):
        draw = plot.PlotCanvas(pnl)
        data1, data2, data3 = test_numpy()
        line1 = plot.PolyLine(data1, colour="red", width=1)
        line2 = plot.PolyLine(data2, colour="green", width=1)
        line3 = plot.PolyLine(data3, colour="blue", width=1)
        a = plot.utils.pairwise(tuple(data1))
        #gc = plot.PlotGraphics([line1, ], "test", "x", "y")
        #gc = plot.PlotGraphics([line1, line2, line3], "test", "x", "y")
        #gc = plot.PlotGraphics([line2, line1, line3], "test", "x", "y")
        gc = plot.PlotGraphics([line3, line2, line1], "test", "x", "y")
        draw.Draw(gc)
        return draw

    def test2_draw(self):
        pass

    def on_move(self, e):
        x, y = e.GetPosition()


if __name__ == '__main__':
    app = wx.App()
    win = MyFrame(None)
    app.MainLoop()