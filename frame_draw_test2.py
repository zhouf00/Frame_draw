import os
import wx
from wx import adv
from wx import grid
from zfdb import *



class MyFrame(wx.Frame):

    # 初始化常量
    __MY_WINDOW = (600, 450)
    __MY_TITLE = "数据库操作"
    __SER_PATH =  ""

    # 初始化变量
    __ser_list = []
    __ser_name = ""
    __con_list = []
    __db_list = []
    __db_name = ""
    __tab_list = []
    __tab_name = ""

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, *kw)
        self.SetTitle(self.__MY_TITLE)
        self.SetSize(self.__MY_WINDOW)
        self.Center()

        self.pnl = wx.Panel(self)
        self.v_sizer = wx.BoxSizer(wx.VERTICAL)
        self.h01_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.h02_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 第一层服务器配置文件选择
        self.__ser_list = self.__show_ser_list()
        print(self.__ser_list)
        self.h01_text = wx.StaticText(self.pnl, label="服务器选择")
        self.h01_sizer.Add(self.h01_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.h01_box = wx.BoxSizer()
        self.h01_box_choice = wx.Choice(self.pnl, choices=self.__ser_list)
        self.h01_box_choice.SetSelection(0)
        self.__ser_name = self.h01_box_choice.GetStringSelection()
        self.h01_box.Add(self.h01_box_choice, 1, wx.EXPAND, 5)
        self.h01_sizer.Add(self.h01_box, 1, wx.EXPAND | wx.ALL, 5)
        self.h01_button = wx.Button(self.pnl, label="连接")
        self.h01_sizer.Add(self.h01_button, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        # 第二层左边列表添加
        self.h02_left = wx.BoxSizer(wx.VERTICAL)
        self.h02_left_list = wx.ListBox(self.pnl, -1, choices=self.__db_list, style=wx.LB_SINGLE)
        self.h02_left.Add(self.h02_left_list, 1, wx.EXPAND | wx.ALL, 5)
        self.h02_sizer.Add(self.h02_left, 0, wx.EXPAND | wx.ALL, 5)

        # 第二层右边列表添加
        self.h02_right = wx.BoxSizer(wx.VERTICAL)
        self.h02_right_list = wx.ListBox(self.pnl, choices=self.__tab_list, style=wx.LB_SINGLE)
        self.h02_right.Add(self.h02_right_list, 1, wx.EXPAND | wx.ALL, 5)
        self.h02_sizer.Add(self.h02_right, 1, wx.EXPAND | wx.ALL, 5)

        # 添加各模块到竖向布局
        self.v_sizer.Add(self.h01_sizer, 0, wx.EXPAND | wx.ALL, 5)
        self.v_sizer.Add(self.h02_sizer, 1, wx.EXPAND | wx.ALL, 5)

        self.pnl.SetSizer(self.v_sizer)

        # 文件菜单
        self.menu = wx.Menu()
        self.add_menu = self.menu.Append(wx.ID_ANY, "新增服务器", "")
        self.menu.AppendSeparator()
        self.menu_bar = wx.MenuBar()
        self.menu_bar.Append(self.menu, "文件")
        self.SetMenuBar(self.menu_bar)
        self.CreateStatusBar()
        self.Show()

        # 事件绑定
        self.Bind(wx.EVT_CHOICE, self.__h01_cho_event, self.h01_box_choice)
        self.Bind(wx.EVT_BUTTON, self.__h01_but_event, self.h01_button)
        self.Bind(wx.EVT_MENU, self.__add_menu_event, self.add_menu)

    def __show_ser_list(self):
        self.file_path = os.path.join(os.getcwd(), ".server")
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)
        return os.listdir(self.file_path)

    def __h01_cho_event(self, e):
        self.__ser_name = self.h01_box_choice.GetStringSelection()

    def __h01_but_event(self, e):
        try:
            con_name = os.path.join(self.file_path, self.__ser_name)
            f = open(con_name, "r")
            self.__con_list = f.readline().split(",")
            self.__mysql = MySql(self.__con_list)
            self.__db_list = self.tup2list(self.__mysql.show_db())
            print(self.__db_list)
            self.h02_left.Clear(True)
            #self.h02_left_list = wx.ListBox(self.pnl, choices=self.__db_list, style=wx.LB_SINGLE)
            #self.h02_left.Add(self.h02_left_list, 1, wx.EXPAND | wx.ALL, 5)
            self.h02_left.Layout()

            # 事件绑定
            self.Bind(wx.EVT_LISTBOX, self.__h02_left_event, self.h02_left_list)

        except Exception as eve:
            wx.MessageBox("输入有误", "错误", wx.OK | wx.ICON_INFORMATION)

    def __h02_left_event(self, e):
        index = e.GetEventObject().GetSelection()
        print(index)
        self.__db_name = self.__db_list[index]
        self.__tab_list = self.tup2list(self.__mysql.show_tab(self.__db_name))
        self.h02_right.Clear(True)
        self.h02_right_list = wx.ListBox(self.pnl, choices=self.__tab_list, style=wx.LB_SINGLE)
        self.h02_right.Add(self.h02_right_list, 1, wx.EXPAND | wx.ALL, 5)
        self.h02_right.Layout()

        # 双击事件绑定
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.__h02_right_event, self.h02_right_list)

    def __h02_right_event(self, e):
        index = e.GetEventObject().GetSelection()
        self.__tab_name = self.__tab_list[index]
        tmp_list = self.__con_list
        tmp_list[4] = self.__db_name
        diglog = MyDialog1(tmp_list, self.__tab_name,self)
        diglog.ShowModal()

    def __add_menu_event(self, e):
        dialog = MyDialog2(self.file_path,self)
        dialog.ShowModal()
        new_list = os.listdir(self.file_path)
        self.h01_box.Clear(True)
        new_choice = wx.Choice(self.pnl, choices=new_list)
        self.h01_box.Add(new_choice, 1, wx.EXPAND, 5)
        self.h01_box.Layout()

    def tup2list(self, in_tup):
        re_list = []
        for var in in_tup:
            re_list.append("".join(tuple(var)))
        return re_list


class MyDialog1(wx.Dialog):

    __con_list = []
    __tab_name = ""
    __start_row = 0
    __end_row = 0
    __sum_row = 0

    # 初始化常量
    __TRUE_COL = 10
    __TRUE_ROW = 25
    __COL_VAL = 75
    __ROW_VAL = 25
    __BOU_VAL = 100
    __BOT_VAL = 100
    __MAX_ROW = 1000

    def __init__(self, con_list, tab_name, *args, **kw):
        super(MyDialog1, self).__init__(*args, **kw)
        self.__con_list = con_list
        self.__tab_name = tab_name

        self.SetTitle("库名：%s<表名：%s>"%(self.__con_list[4],self.__tab_name))
        self.ms = MySql(self.__con_list)
        self.tab_data = self.ms.FindAll(self.__tab_name)
        self.headline = self.ms.show_headline(self.__tab_name)
        self.m_cols = len(self.tab_data[0])-1
        self.m_rows = len(self.tab_data)

        self.SetSize(self.true_size())

        # 添加布局
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.gv_sizer = wx.BoxSizer(wx.VERTICAL)
        self.gh01_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.gh03_sizer = wx.BoxSizer(wx.VERTICAL)
        self.gh04_sizer = wx.BoxSizer(wx.HORIZONTAL)

        ################################################
        # 翻页按键
        ################################################
        self.gh01_button1 = wx.Button(self, wx.ID_ANY, "显示数据")
        self.gh01_sizer.Add(self.gh01_button1,0, wx.EXPAND | wx.ALL, 5)
        self.gh01_sizer.AddStretchSpacer(1)
        """
        self.gh01_button2 = wx.Button(self, label="上一页")
        self.gh01_sizer.Add(self.gh01_button2, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        self.gh01_button3 = wx.Button(self, label="下一页")
        self.gh01_sizer.Add(self.gh01_button3, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        """
        self.gv_sizer.Add(self.gh01_sizer, 0, wx.EXPAND | wx.ALL, 5)

        ################################################
        # 删除操作（时间与按键）
        ################################################
        self.gh02_sizer = wx.StaticBoxSizer(wx.StaticBox(self, 0, label="删除操作"), wx.HORIZONTAL)

        start_text_time = wx.StaticText(self, label="开始时间",style=wx.ALIGN_CENTER)
        self.gh02_sizer.Add(start_text_time, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.start_time = adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             adv.DP_DEFAULT)
        self.gh02_sizer.Add(self.start_time, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        end_text_time = wx.StaticText(self, label="结束时间", style=wx.ALIGN_CENTER)
        self.gh02_sizer.Add(end_text_time, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.end_time = adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                             adv.DP_DEFAULT)
        self.gh02_sizer.Add(self.end_time, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.gh02_button = wx.Button(self, wx.ID_ANY, "删除")
        self.gh02_sizer.Add(self.gh02_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.gv_sizer.Add(self.gh02_sizer, 0, wx.EXPAND | wx.ALL, 5)

        self.m_grid = self.create_grid(bool=False)
        self.gh03_sizer.Add(self.m_grid, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.gv_sizer.Add(self.gh03_sizer, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)

        ################################################
        # 布局汇合
        ################################################
        self.SetSizer(self.gv_sizer)
        self.Layout()
        self.Center(wx.BOTH)

        # 事件绑定
        self.Bind(wx.EVT_BUTTON, self.__show_grid, self.gh01_button1)
        self.Bind(wx.EVT_BUTTON, self.__del_data, self.gh02_button)

    def __show_grid(self, e):
        self.gh03_sizer.Clear(True)
        self.m_grid = self.create_grid()
        self.gh03_sizer.Add(self.m_grid, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.ALL, 5)
        self.gh03_sizer.Layout()

    def __del_data(self, e):
        start_time = self.start_time.GetValue().GetTicks() * 1000
        end_time = self.end_time.GetValue().GetTicks() * 1000
        try:
            self.ms.time_del((self.__tab_name, self.headline[2], start_time,
                              self.headline[2], end_time))
        except Exception as event:
            wx.MessageBox("数据不存在","错误", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("数据删除成功","完成", wx.OK | wx.ICON_INFORMATION)

    def __up_data(self, e):
        pass

    def __next_data(self, e):
        pass

    def create_grid(self, bool=True):
        if self.__start_row == 0:
            if self.m_rows < 1000:
                self.__end_row = self.m_rows
            else:
                self.__end_row = self.__MAX_ROW
        m_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        m_grid.CreateGrid(self.__end_row, self.m_cols)
        col_name = self.headline
        print("start:%s, end:%s"%(self.__start_row,self.__end_row))
        print("col:%s"%len(self.tab_data[self.__start_row]))
        if bool is True:
            i = 0
            for row in range(self.__start_row, self.__end_row):
                m_grid.SetRowLabelValue(row, str(self.tab_data[row][0]))  # 确保序列号与数据库id保持一致
                for col in range(1, len(self.tab_data[row])):
                    m_grid.SetColLabelValue(col - 1, col_name[col])
                    m_grid.SetCellValue(i, col - 1, str(self.tab_data[row][col]))
                i += 1
            self.__sum_row += self.__end_row
            tmp = self.m_rows - self.__sum_row
            if tmp > 1000:
                self.__start_row += self.__MAX_ROW
                self.__end_row += self.__MAX_ROW
            elif tmp > 0 and tmp < 1000:
                self.__start_row += tmp
                self.__end_row += self.__MAX_ROW
            self.gh03_sizer.Layout()
        return m_grid

    def true_size(self):
        if self.m_cols > self.__TRUE_COL:
            g_col = (self.__TRUE_COL + 1) * self.__COL_VAL + self.__BOU_VAL
        elif self.m_cols < self.__TRUE_COL - 4:
            g_col = (self.__TRUE_COL - 5) * self.__COL_VAL + self.__BOU_VAL
        else:
            g_col = (self.m_cols + 1) * self.__COL_VAL + self.__BOU_VAL

        if self.m_rows > self.__TRUE_ROW:
            g_row = self.__BOT_VAL + (self.__TRUE_ROW + 1) * self.__ROW_VAL + self.__BOU_VAL
        else:
            g_row = self.__BOT_VAL + (self.m_rows + 1) * self.__ROW_VAL + self.__BOU_VAL
        return g_col, g_row


class MyDialog2(wx.Dialog):

    con_list = []

    def __init__(self, file_path, *args, **kw):
        super(MyDialog2, self).__init__(*args, **kw)

        self.__file_path = file_path

        self.SetTitle("创建完成，请关闭程序，重新开启")
        self.SetSize((400,450))

        self.pnl = wx.Panel(self)
        self.gSizer = wx.BoxSizer(wx.VERTICAL)
        self.gSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.ip = wx.TextCtrl(self.pnl, size=(210, 25))
        self.port = wx.TextCtrl(self.pnl, size=(210, 25))
        self.port.SetValue("3306")
        self.user = wx.TextCtrl(self.pnl, size=(210, 25))
        self.pwd = wx.TextCtrl(self.pnl, size=(210, 25))
        self.name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.add_affirm = wx.Button(self.pnl, label="添加", size=(80, 25))
        # 为添加按钮组件绑定事件处理
        self.add_affirm.Bind(wx.EVT_BUTTON, self.addaffirm)
        #################################################################################
        # 创建静态框
        ser_ip = wx.StaticBox(self.pnl, label="服务器IP")
        ser_port = wx.StaticBox(self.pnl, label="服务器端口")
        ser_user = wx.StaticBox(self.pnl, label="服务器用户名")
        ser_pwd = wx.StaticBox(self.pnl, label="密码")
        ser_name = wx.StaticBox(self.pnl, label="保存名字")
        # 创建水平方向box布局管理器
        hsbox_ip = wx.StaticBoxSizer(ser_ip, wx.HORIZONTAL)
        hsbox_port = wx.StaticBoxSizer(ser_port, wx.HORIZONTAL)
        hsbox_user = wx.StaticBoxSizer(ser_user, wx.HORIZONTAL)
        hsbox_pwd = wx.StaticBoxSizer(ser_pwd, wx.HORIZONTAL)
        hsbox_name = wx.StaticBoxSizer(ser_name, wx.HORIZONTAL)
        # 添加到hsbox布局管理器
        hsbox_ip.Add(self.ip, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_port.Add(self.port, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_user.Add(self.user, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_pwd.Add(self.pwd, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_name.Add(self.name, 0, wx.EXPAND | wx.BOTTOM, 5)

        self.gSizer.Add(hsbox_ip, 0, wx.CENTER | wx.ALL, 5)
        self.gSizer.Add(hsbox_port, 0, wx.CENTER  | wx.ALL, 5)
        self.gSizer.Add(hsbox_user, 0, wx.CENTER | wx.ALL, 5)
        self.gSizer.Add(hsbox_pwd, 0, wx.CENTER  | wx.ALL, 5)
        self.gSizer.Add(hsbox_name, 0, wx.CENTER | wx.ALL, 5)
        self.gSizer.Add(self.add_affirm, 0, wx.CENTER | wx.ALL, 5)

        self.pnl.SetSizer(self.gSizer)

    def addaffirm(self, e):
        self.con_list.clear()
        self.con_list.append(self.ip.GetValue())
        self.con_list.append(self.port.GetValue())
        self.con_list.append(self.user.GetValue())
        self.con_list.append(self.pwd.GetValue())
        # db 为空
        self.con_list.append("-")
        ser_name = os.path.join(self.__file_path,self.name.GetValue())
        try:
            if len(ser_name) > 0:
                if not os.path.isfile(ser_name):
                    f = open(ser_name, "w")
                    f.writelines(','.join(self.con_list))
                    f.close()
        except Exception:
            wx.MessageBox("输入有误", "错误", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("保存成功", "成功", wx.OK | wx.ICON_INFORMATION)
            self.Close()

if __name__ == '__main__':
    app = wx.App()
    win = MyFrame(None)
    app.MainLoop()

