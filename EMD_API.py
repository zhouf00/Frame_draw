import os
from random import sample
import numpy as np
import time


class ParaEMD(object):

    mylist = []

    def __init__(self):
        self.FengChang = ['茶山', '桃山', "花果山"]
        #self.IdFan = ['1', '2', '3', '4', '5', '6'] #文本框输入风机编号
        self.wind_machine = {"茶山": ["大别山", "天目山"],
                        "桃山": ["昆仑山", "三清山"],
                        "花果山": ["五指山", "火焰山"]}
        self.IdBlade = ['X-20','X-1K', 'Y-20', 'Y-1K']
        self.TypeData = ['振动','包络' ]
        self.LblList = ['分量1', '分量2', '分量3',]
        self.LblListLcn = ['叶片1', '叶片2', '叶片3']

    def tmp_list(self):
        return self.mylist

    def bbb(self):
        data1 = np.random.rand(2,2)
        return data1

    def wind_mach_chooice(self, val):
        return self.wind_machine[val]

    def LoadData(self, *args):
        file_path = os.path.join(os.getcwd(), "风机采集信号数据\\1K")
        file_list = os.listdir(file_path)
        file_list = [var for var in file_list if var.split(".")[1] == "csv"]
        a = []
        for var in file_list:
            tmp = os.path.join(file_path, var)
            rd_file = np.loadtxt(tmp, delimiter=",", usecols=(0, 1))
            a.append(rd_file)
        return a[0], a[1], a[2]

    def EMDTRS(self, *args):
        res = ["20190501", "20190502", "20190504", "20190508", "20190515"]
        for var in res:
            self.mylist.append(var)


    def test1_data(self):
        file_path = os.path.join(os.getcwd(), "data\\1K")
        file_name = os.path.join(file_path, "1K_FFT1.csv")
        return file_name