import os
import numpy as np
import pandas as pd
from scipy.io import loadmat


def CWRU(item_path):
    axis = ["_DE_time", "_FE_time", "_BA_time"]
    datanumber = os.path.basename(item_path).split(".")[0]
    if eval(datanumber) < 100:
        realaxis = "X0" + datanumber + axis[0]
    else:
        realaxis = "X" + datanumber + axis[0]
    signal = loadmat(item_path)[realaxis]

    return signal


def MFPT(item_path):
    f = item_path.split("/")[-2]
    if f == 'normal':
        signal = (loadmat(item_path)["bearing"][0][0][1])
    else:
        signal = (loadmat(item_path)["bearing"][0][0][2])

    return signal
