# Author: xumingda
#!/usr/bin/env python
# -*-  coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = open(r'D:\TJU\学习\GITHUB\01\PLC\plc.csv')
Hlength=len(a.readlines())
data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values

# print(len(data_x),len(data_z),len(data_y)) #110027



