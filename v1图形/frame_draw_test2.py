import wx
from threading import Thread
from wx import adv
from EMD_API import ParaEMD
from v1图形.wxplot_test1 import Plot_Pnl  #

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
        hb3_text8 = wx.StaticBoxSizer(wx.StaticBox(pnl, 0, label=u"幅值选择"),wx.HORIZONTAL)
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
        self.hb3_v_draw1 = Plot_Pnl(pnl)
        self.hb3_v_draw2 = Plot_Pnl(pnl)
        hb3_v2.AddMany([(self.hb3_v_draw1, 2, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
                        (self.hb3_v_draw2, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5),
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
        self.left = [pnl, hb3_text6]
        self.right = [pnl, hb3_v2]

    def _func_event(self):
        #self.Bind(wx.EVT_MOVE, self.on_move)
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
        start_thread = Thread(target=self._start_func,
                               args=(wind_f, wind_m, wind_b, signal_t, begin_t, end_t,))
        start_thread.start()
        self.left[1].Clear(True)
        self.hb3_v_ch7 = wx.Choice(self.left[0], choices=ParaEMD().aaa())
        self.left[1].Add(self.hb3_v_ch7, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.left[1].Layout()

    def _show_event(self, e):
        fl_list1 = self.hb3_v_box1.GetSelection()
        data_list_all =[]
        float_value =[]
        
        data_list_all.append(self.hb3_v_ch3.GetSelection())
        data_list_all.append(self.hb3_v_ch4.GetSelection())
        data_list_all.append(self.hb3_v_ch5.GetSelection())
        time_list1 = self.hb3_v_ch7.GetStringSelection()
        float_value.append(self.hb3_v_lc9.GetValue())
        float_value.append(self.hb3_v_lc11.GetValue())
        fanid = self.hb1_listc6.GetStringSelection()
        self._show_func(fl_list1, data_list_all, time_list1, float_value, fanid)

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
        ParaEMD().EMDTRS(location, fan, fanid, typedata, start_time, end_time)
        ParaEMD().EMDTRS()

    def _show_func(self, *args):
        """
        显示函数，外部函数实现，传入参数
        :param args: IMF值， 优先级列表[1、2、3]，时间，幅值列表,分类
        :return:
        """

        IMF_value, pri_value, ft_value, flt_list, fanid= args
        print(args)
        draw_thread1 = Thread(target=self.test1_draw,
                              args=(ParaEMD().LoadData(ft_value,fanid,IMF_value), pri_value))
        #draw_thread2 = Thread(target=self.test2_draw,
         #                       args=(ParaEMD().test_numpy()[0],))
        draw_thread1.start()
        #draw_thread2.start()

    def test2_draw(self, args):
        self.hb3_v_draw2._draw_new_one(args)

    def test1_draw(self, args, pri_val):
        self.hb3_v_draw1._draw_new(args, pri_val)


if __name__ == '__main__':
    app = wx.App()
    win = MyFrame(None)
    app.MainLoop()