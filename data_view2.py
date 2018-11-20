# Author: xumingda
#!/usr/bin/env python
# -*-  coding:utf-8 -*-
# 刀具剩余寿命比赛，振动信号 电流信号 的可视化

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
a = open(r'D:\TJU\学习\GITHUB\01\PLC\plc.csv')
Hlength=len(a.readlines())

data_load= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
time= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["time"].values

#        vibration_1	vibration_2  	vibration_3  	current
a = open(r'D:\TJU\学习\GITHUB\01\Sensor\1.csv')
Hlength=len(a.readlines())
os.chdir(r'D:\TJU\学习\GITHUB\01\Sensor')
#设置当前环境路径
vibration_x= pd.read_csv(filepath_or_buffer = '33.csv', sep = ',')["vibration_1"].values
vibration_y= pd.read_csv(filepath_or_buffer = '33.csv', sep = ',')["vibration_3"].values
vibration_z= pd.read_csv(filepath_or_buffer = '33.csv', sep = ',')["vibration_2"].values
current= pd.read_csv(filepath_or_buffer = '33.csv', sep = ',')["current"].values





# 画图 xyz振动信号 电流信号
# fig = plt.figure()
# plt.subplot(411)
# plt.plot(vibration_x,lw=0.1)
# plt.plot(vibration_x,'')
# plt.grid(True)
# plt.axis('tight')
# plt.xlabel('time')
# plt.ylabel('vibration_x')
# plt.title('vibration_x')

# plt.subplot(412)
# plt.plot(vibration_y,lw=0.1)
# plt.plot(vibration_y,'r')
# plt.grid(True)
# plt.axis('tight')
# plt.xlabel('time')
# plt.ylabel('vibration_y')
# plt.title('vibration_y')

# plt.subplot(413)
# plt.plot(vibration_z,lw=2)
# plt.plot(vibration_z,'ro')
# plt.grid(True)
# plt.axis('tight')
# plt.xlabel('time')
# plt.ylabel('vibration_z')
# plt.title('vibration_z')
# #
# plt.subplot(414)
# plt.plot(current,lw=0.1)
# plt.plot(current,'r')
# plt.grid(True)
# plt.axis('tight')
# plt.xlabel('time')
# plt.ylabel('current')
# plt.title('current')
#
#
# plt.show()

# #振动信号矢量图
# mpl.rcParams['legend.fontsize'] = 10
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = vibration_z
# x = vibration_x
# y = vibration_y
# ax.set_title('3D shiliang')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
#
# plt.show()