import wx
from threading import Thread
from wx import adv
from wx.lib import plot
from Matplotlib_test2 import *
from test_data import *
from EMD_API import ParaEMD

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.SetSize((800, 650))
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
        hb3_v2 = wx.BoxSizer(wx.VERTICAL)

        ######################################
        # 第一层 配置文件
        ######################################
        text1 = wx.StaticText(pnl, wx.ID_ANY, u"风场")
        self.hb1_listc2 = wx.Choice(pnl, choices=ParaEMD().FengChang)
        self.hb1_listc2.SetSelection(0)
        text3 = wx.StaticText(pnl, wx.ID_ANY, u"风机")
        self.hb1_textc4 = wx.TextCtrl(pnl)
        text5 = wx.StaticText(pnl, wx.ID_ANY, u"叶片ID")
        self.hb1_listc6 = wx.Choice(pnl, choices=ParaEMD().IdBlade)
        self.hb1_listc6.SetSelection(0)
        text7 = wx.StaticText(pnl, wx.ID_ANY, u"信号类型")
        self.hb1_listc8 = wx.Choice(pnl, choices=ParaEMD().TypeData)
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
        # 第二层 时间
        ######################################
        text9 = wx.StaticText(pnl, wx.ID_ANY, u"起始:")
        self.hb2_time10 = adv.DatePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                            wx.DefaultPosition, wx.DefaultSize, adv.DP_DEFAULT)
        text11 = wx.StaticText(pnl, wx.ID_ANY, u"结束：")
        self.hb2_time12 = adv.DatePickerCtrl(pnl, wx.ID_ANY, wx.DefaultDateTime,
                                                    wx.DefaultPosition, wx.DefaultSize, adv.DP_DEFAULT)
        self.hb2_button13 = wx.Button(pnl, label=u"运行")

        hb2.AddMany([(text9, 0, wx.ALIGN_CENTER | wx.ALL, 10),
                     (self.hb2_time10, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (text11, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb2_time12, 0, wx.ALIGN_CENTER | wx.ALL, 5),
                     (self.hb2_button13, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                                          ])

        ######################################
        # 第三层左侧 配置文件
        ######################################
        self.hb3_v_box1 = wx.RadioBox(pnl, label=u"IMF分量",
                                        choices=ParaEMD().LblList, majorDimension = 3, style = wx.RA_SPECIFY_ROWS)
        hb3_text2 = wx.StaticBoxSizer(wx.StaticBox(pnl, 0, label=u"显示优先级"), wx.VERTICAL)
        self.hb3_v_ch3 = wx.Choice(pnl, choices=ParaEMD().LblListLcn)
        self.hb3_v_ch3.SetSelection(0)
        self.hb3_v_ch4 = wx.Choice(pnl, choices=ParaEMD().LblListLcn)
        self.hb3_v_ch4.SetSelection(1)
        self.hb3_v_ch5 = wx.Choice(pnl, choices=ParaEMD().LblListLcn)
        self.hb3_v_ch5.SetSelection(2)
        hb3_text6 = wx.StaticBoxSizer(wx.StaticBox(pnl, 0, label=u"时间选择"), wx.VERTICAL)
        self.hb3_v_ch7 = wx.Choice(pnl, choices=[])
        #self.hb3_v_ch7 = wx.ListBox(pnl, choices=[], style=wx.LB_SINGLE)
        hb3_text8 = wx.StaticBoxSizer(wx.StaticBox(pnl, 0, label=u"浮值选择"),wx.HORIZONTAL)
        self.hb3_v_lc9 = wx.TextCtrl(pnl, size=(50, 25), value="100")
        hb3_text8_line = wx.StaticText(pnl, label=u"----")
        self.hb3_v_lc11 = wx.TextCtrl(pnl,  size=(50, 25), value="400")
        self.hb3_v_button6 = wx.Button(pnl, label=u"显示")

        hb3_text2.AddMany([(self.hb3_v_ch3, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           (self.hb3_v_ch4, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           (self.hb3_v_ch5, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           ])
        hb3_text6.AddMany([(self.hb3_v_ch7, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           ])
        hb3_text8.AddMany([(self.hb3_v_lc9, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           (hb3_text8_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           (self.hb3_v_lc11, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           ])

        hb3_v1.AddMany([(self.hb3_v_box1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (hb3_text2, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (hb3_text6, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (hb3_text8, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (self.hb3_v_button6, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                           ])
        ######################################
        # 第三层右侧 配置文件
        ######################################
        hb3_v_draw1 = self.test_draw(pnl)
        hb3_v_draw2 = self.test2_draw(pnl)
        hb3_v2.AddMany([(hb3_v_draw1, 2, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (hb3_v_draw2, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        ])
        ######################################
        # 所有面板汇合
        ######################################
        h1_line = wx.StaticLine(pnl, wx.ID_ANY)
        h2_line = wx.StaticLine(pnl,wx.ID_ANY, style=wx.LI_VERTICAL)
        hb3.AddMany([(hb3_v1, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                     (h2_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                     (hb3_v2, 3, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),])
        vb.AddMany([(hb1, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (hb2, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (h1_line, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    (hb3, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                    ])
        pnl.SetSizer(vb)
        self.CreateStatusBar()

        #　传面板参数
        self.res = [pnl, hb3_text6, hb3_v1]

    def _func_event(self):
        self.Bind(wx.EVT_MOVE, self.on_move)
        self.hb2_button13.Bind(wx.EVT_BUTTON, self._start_event)
        self.hb3_v_button6.Bind(wx.EVT_BUTTON, self._show_event)

    def _start_event(self, e):
        wind_f = self.hb1_listc2.GetStringSelection()
        wind_m = self.hb1_textc4.GetValue()
        wind_b = self.hb1_listc6.GetStringSelection()
        signal_t = self.hb1_listc8.GetStringSelection()
        begin = self.hb2_time10.GetValue()
        begin_t = "%s/%s/%s"%(begin.year, str(int(begin.month)+1), begin.day)
        end = self.hb2_time12.GetValue()
        end_t = "%s/%s/%s"%(end.year, str(int(end.month)+1), end.day)
        #self._start_func(wind_f, wind_m, wind_b, signal_t, begin_t, end_t)
        _start_thread = Thread(target=self._start_func,
                               args=(wind_f, wind_m, wind_b, signal_t, begin_t, end_t,))
        _start_thread.start()
        a = ParaEMD().aaa()

        self.res[1].Clear(True)
        self.hb3_v_ch7 = wx.Choice(self.res[0], choices=a)
        self.res[1].Add(self.hb3_v_ch7, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.res[1].Layout()

    def _show_event(self, e):
        a = self.hb3_v_box1.GetSelection()
        fl_list1 = ParaEMD().LblList[a]
        data_list_all =[]
        data_list_all.append(self.hb3_v_ch3.GetStringSelection())
        data_list_all.append(self.hb3_v_ch4.GetStringSelection())
        data_list_all.append(self.hb3_v_ch5.GetStringSelection())
        time_list1 = self.hb3_v_ch7.GetStringSelection()
        self._show_func(fl_list1, data_list_all, time_list1)

    def _start_func(self, *args):
        """
        引入外部函数，传入参数
        :param args: 风场、风机、叶片、信号、开始时间、结束时间
        :return:
        """
        location = args[0]
        fan = args[1]
        fanid = args[2]
        typedata = args[3]
        start_time = args[4]
        end_time = args[5]
        #ParaEMD().EMDTRS(location, fan, fanid, typedata, start_time, end_time)

    def _show_func(self, *args):
        """
        显示函数，外部函数实现，传入参数
        :param args: IMF值， 优先级1、2、3
        :return:
        """
        for var in args[1]:
            print(var)
        pass

    def test_draw(self, pnl):
        draw = plot.PlotCanvas(pnl)
        data1, data2, data3 = test_numpy()
        line1 = plot.PolyLine(data1, colour="red", width=1)
        line2 = plot.PolyLine(data2, colour="green", width=1)
        line3 = plot.PolyMarker(data3, colour="blue", width=1,
                                marker='circle', size=1)

        #a = plot.utils.pairwise(tuple(data1))
        #gc = plot.PlotGraphics([line1, ], "test", "x", "y")
        #gc = plot.PlotGraphics([line1, line2, line3], "test", "x", "y")
        #gc = plot.PlotGraphics([line2, line1, line3], "test", "x", "y")
        gc = plot.PlotGraphics([line3, line2, line1], "test", "x", "y")
        draw.Draw(gc)
        return draw

    def test2_draw(self, pnl):
        draw = plot.PlotCanvas(pnl)
        data1 = ParaEMD().bbb()
        ab = plot.PolyLine(data1, colour="red",  drawstyle="line")
        gc = plot.PlotGraphics([ab,], "test", "x", "y")
        draw.Draw(gc)
        return draw

    def on_move(self, e):
        x, y = e.GetPosition()


if __name__ == '__main__':
    app = wx.App()
    win = MyFrame(None)
    app.MainLoop()