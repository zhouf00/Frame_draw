import os
import numpy as np
import pandas as pd

file_path = os.path.join(os.getcwd(), "data\\1K")
file_name = os.path.join(file_path, "1K_FFT1.csv")

wind_field = ["风场1", "风场2", "风场3"]
wind_machine = {"风场1":["大别山", "天目山"],
                "风场2":["昆仑山", "三清山"],
                "风场3":["五指山", "火焰山"]}
wind_blade = ["X-20Hz", "X-1K", "Y-20Hz", "Y-1K"]
signal_type = ["包络", "振动"]

tmp_time_list = ["20190501", "20190502", "20190504", "20190508", "20190515"]

def wind_mach_chooice(val):
    return wind_machine[val]

def _read_data():
    file_list = os.listdir(file_path)
    file_list = [var for var in file_list if var.split(".")[1] == "csv"]
    a = []
    for var in file_list:
        tmp = os.path.join(file_path, var)
        rd_file = np.loadtxt(tmp, delimiter=",", usecols=(0, 1))
        a.append(rd_file)
    return a[0], a[1], a[2]

def tmp_file():
    return file_name

def read_pandas():
    #file_name = os.path.join(file_path, "1K_FFT1.csv")

    pd_file = pd.read_csv(file_name)
    df = pd.DataFrame(pd_file)

    for i in range(df.shape[1]):
        pass
        #print(df.iloc[:,i])
    xdict = dict(enumerate(df.aa))
    bb = df.iloc[:, 0][64901].astype(str)
    abc = "<p style='color:white'>日期：{0}</p>" \
          "<p style='color:white'>开盘：{1}</p>" \
          "<p style='color:white'>收盘：{2}</p>" \
          "<p style='color:white'>收盘：{3}</p>".format(df.iloc[:, 0][100].astype(str),
            df.iloc[:, 1][100].astype(str),
            df.iloc[:, 2][100].astype(str),
            df.iloc[:, 3][100].astype(str))
    print(type(bb))
    print(abc)

def test():
    self.label.setHtml("<p style='color:white'>日期：{0}</p>\
                                                <p style='color:white'>开盘：{1}</p>\
                                                <p style='color:white'>收盘：{2}</p>\
                                               <p style='color:white'>收盘：{3}</p>"
                       .format(self.data.iloc[:, 0][index].astype(str),
                               self.data.iloc[:, 1][index].astype(str),
                               self.data.iloc[:, 2][index].astype(str),
                               self.data.iloc[:, 3][index].astype(str)))

if __name__ == '__main__':
    #_wind_mach_chooice("风场1")
    read_pandas()
