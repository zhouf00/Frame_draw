import os
from random import sample
import numpy as np


class ParaEMD(object):

    def __init__(self):
        self.FengChang = ['国电电力宁海茶山风电场', '华能围场桃山湖风电场']
        #self.IdFan = ['1', '2', '3', '4', '5', '6'] #文本框输入风机编号
        self.IdBlade = ['X-20','X-1K', 'Y-20', 'Y-1K']
        self.TypeData = ['振动','包络' ]
        self.LblList = ['分量1', '分量2', '分量3']
        self.LblListLcn = ['叶片1', '叶片2', '叶片3']

    def aaa(self):
        res = ["2019-5-20", "2019-5-21", "2019-5-22", "2019-5-24", "2019-5-25"]
        return res

    def bbb(self):
        data1 = np.random.rand(2,2)
        return data1

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