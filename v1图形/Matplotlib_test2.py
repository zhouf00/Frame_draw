import os
import numpy as np


file_path = os.path.join(os.getcwd(), "风机采集信号数据\\1K")

def test_numpy():
    file_list = os.listdir(file_path)
    file_list = [var for var in file_list if var.split(".")[1] == "csv"]
    a = []
    for var in file_list:
        tmp = os.path.join(file_path, var)
        rd_file = np.loadtxt(tmp, delimiter=",",usecols=(0,1))
        a.append(rd_file)
    return a[0], a[1], a[2]


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), "风机采集信号数据\\1K")
    a = os.listdir(file_path)
    b = [var for var in a if var.split(".")[1] == "csv"]
    print(b)
    # test_numpy()