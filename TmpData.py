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
        print(df.iloc[:,i])
    #print(list(df["1x"]))
    print("data",df.index)

if __name__ == '__main__':
    #_wind_mach_chooice("风场1")
    read_pandas()
