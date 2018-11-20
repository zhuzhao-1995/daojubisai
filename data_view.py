# Author: xumingda
#!/usr/bin/env python
# -*-  coding:utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:37:21 2015

@author: Eddy_zheng
"""


# 刀具剩余寿命比赛 刀具行走轨迹，主轴负载曲线

from matplotlib import pyplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


# #--------------------训练集 1号刀
# a = open(r'E:\huawei-bisai\01-TrainingData-qLua\01-TrainingData-qLua\01\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()


# #-----------------------训练集 2号刀
# a = open(r'E:\huawei-bisai\01-TrainingData-qLua\01-TrainingData-qLua\02\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()



# # #-----------------训练集 3号刀
# a = open(r'E:\huawei-bisai\01-TrainingData-qLua\01-TrainingData-qLua\03\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# # #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# # #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()

# # #-----------------测试集 1号刀
# a = open(r'E:\huawei-bisai\02-TestingData-poL3\02-TestingData-poL3\01\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# # #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# # #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()


# #-----------------测试集 2号刀
# a = open(r'E:\huawei-bisai\02-TestingData-poL3\02-TestingData-poL3\02\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# # #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# # #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()

# #-----------------测试集 3号刀
# a = open(r'E:\huawei-bisai\02-TestingData-poL3\02-TestingData-poL3\03\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# # #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# # #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()

# #-----------------测试集 4号刀
# a = open(r'E:\huawei-bisai\02-TestingData-poL3\02-TestingData-poL3\04\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# # #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# # #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()

# #-----------------测试集 5号刀
# a = open(r'E:\huawei-bisai\02-TestingData-poL3\02-TestingData-poL3\05\PLC\plc.csv')
# Hlength=len(a.readlines())
# data_x= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["x"].values
# data_y= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["y"].values
# data_z= pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["z"].values
# data_load=pd.read_csv(filepath_or_buffer = 'plc.csv', sep = ',')["spindle_load"].values
# print(type(data_x))
# # #-----------------刀具行走路线
# mpl.rcParams['legend.fontsize'] = 10
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# z = data_z
# x = data_x
# y = data_y
# ax.set_title('3D tools Curve')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()
# # #-----------------主轴负载二维图
# fig = plt.figure()
# data_d = data_load
# plt.plot(data_d)
# plt.show()
