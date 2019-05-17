import wx
from threading import Thread
from wx import adv
from test_data import *


class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.SetSize((700, 450))
        self.SetTitle("风机采集图形化")

        # 面板设计
        self._init_frame()

        # 事件绑定

        self.Center()
        self.Show()

    def _init_frame(self):
        # 设置面板各个功能
        pnl = wx.Panel(self)
        vb = wx.BoxSizer(wx.VERTICAL)
        hb1 = wx.BoxSizer(wx.HORIZONTAL)
        hb2 = wx.BoxSizer(wx.HORIZONTAL)

        ######################################
        # 第一层 配置文件
        ######################################
        text1 = wx.StaticText(pnl, wx.ID_ANY, u"风场")
        print(wind_field)
        self.hb1_listc2 = wx.Choice(pnl, choices=wind_field)
        self.hb1_listc2.SetSelection(0)
        text3 = wx.StaticText(pnl, wx.ID_ANY, u"风机")
        self.hb1_textc4 = wx.TextCtrl(pnl)
        text5 = wx.StaticText(pnl, wx.ID_ANY, u"叶片ID")
        self.hb1_listc6 = wx.Choice(pnl, choices=wind_blade)
        text7 = wx.StaticText(pnl, wx.ID_ANY, u"信号类型")
        self.hb1_listc8 = wx.Choice(pnl, choices=signal_type)
        text9 = wx.StaticText(pnl, wx.ID_ANY, u"时间")
        self.hb1_time10 = adv.DatePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                            wx.DefaultPosition, wx.DefaultSize, adv.DP_DEFAULT)



        hb1.AddMany([(text1,  0, wx.ALIGN_CENTER | wx.ALL, 10),
                     (self.hb1_listc2, 0, wx.EXPAND | wx.ALL, 5),
                     (text3, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_textc4, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text5, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_listc6, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text7, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_listc8, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text9, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb1_time10, 0, wx.ALIGN_CENTER | wx.ALL, 5),])

        ######################################
        # 第二层 配置文件
        ######################################


        vb.AddMany([(hb1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (hb2, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    ])
        pnl.SetSizer(vb)
        self.CreateStatusBar()


if __name__ == '__main__':
    app = wx.App()
    win = MyFrame(None)
    app.MainLoop()