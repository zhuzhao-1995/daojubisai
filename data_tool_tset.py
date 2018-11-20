# Author: xumingda
#!/usr/bin/env python
# -*-  coding:utf-8 -*-

#对大量数据进行拼接预处理,数据预处理
from __future__ import print_function
# import keras
# from sklearn.cross_validation import train_test_split
# from keras.preprocessing import sequence
# from keras.models import Sequential
# from keras import utils as np_utils
# from keras.optimizers import Adam
# from keras.layers import Dense, Dropout, Activation
# from keras.layers import Embedding, Flatten
# from keras.layers import Conv1D, GlobalMaxPooling1D
# from keras.layers import Convolution2D, MaxPooling2D
import csv
import numpy as np
import pandas as pd
import os
import sys



#获取文件中的xyz振动信号和电流信号，进行拼接，形成大样本
def get_data(file):
    with open(file, encoding='utf-8') as csvfile:
        vibration_x = pd.read_csv(filepath_or_buffer=file, sep=',')["vibration_1"].values
        vibration_y = pd.read_csv(filepath_or_buffer=file, sep=',')["vibration_3"].values
        vibration_z = pd.read_csv(filepath_or_buffer=file, sep=',')["vibration_2"].values
        current = pd.read_csv(filepath_or_buffer=file, sep=',')["current"].values
    vibration_x = vibration_x.reshape(1, -1)
    vibration_y = vibration_y.reshape(1, -1)
    vibration_z = vibration_z.reshape(1, -1)
    current = current.reshape(1, -1)
    data = vibration_x
    data = np.vstack((data, vibration_y))
    data = np.vstack((data, vibration_z))
    data = np.vstack((data, current))
    # print(data)
    # print(type(data), data.shape)
    return data
#     print(type(vibration_x),vibration_x.shape)
#     print(type(vibration_y),vibration_y.shape)
#     print(type(vibration_z),vibration_z.shape)
#     print(type(current),current.shape)



#定义数据格式转化，转化成  (-1,4,32,32)
def init_data(data,num):
    if data.shape[1]%num == 0:
        data=data.reshape(-1,4,32,32)
    else:
            #除法向下取整，判断一个csv文件之中能取多少个样本
        a=data.shape[1]//num
            # print(a)
            #对数据进行切片处理，取样本数的整数倍数据，后面的不要了
        data=data[:,:a*num]
        data=data.reshape(-1,4,32,32)
    return data



#设置当前目录，在当前目录中进行寻找文件的操作
os.chdir(r'D:\TJU\学习\GITHUB\01\Sensor')
# 所有csv文件名称列表 <class 'list'>
# 获取文件夹内部有的文件的名称，存到 list 中
file_list=os.listdir(r'D:\TJU\学习\GITHUB\01\Sensor')
#知道一共有多少个文件 --->文件数量
file_list_num=len(file_list)
# print(len(file_list))#一共有多少个文件名
# print(file_list)

#设置训练X_train
#设置一个数组X，4维数组， 4 对应的是xyz和电流，32x32是为了贴合CNN 处理

X_train=[]
X_train=np.array(X_train).reshape(-1,4,32,32)
#获得特征数据 X 就是好多点啦
for file in file_list:
    b=get_data(file)
    c=init_data(b,1024)
    X_train=np.vstack((X_train,c))
print(X_train.shape)


#获得特征数据 对应的 标签 label
#    起点        终点        数量
#     1,  file_list_num,   file_list_num
i_num = np.linspace(1,file_list_num,file_list_num)
y1=[]
#y1用来暂时存变量的
y1=np.array(y1).reshape(-1,1)
y_label=[]
y_label=np.array(y_label).reshape(-1,1)
#贴上数据标签，1 - 48
for i in i_num:
    # y1用来暂时存变量的
    y1 = []
    y1 = np.array(y1).reshape(-1, 1)
    b=get_data(file_list[int(i-1)])
    # print(i,b.shape)
    c=init_data(b,1024)
    # print(i,c.shape)
    y1 = i * np.ones((c.shape[0],1), dtype = np.int)
    # print(y1,i,y1.shape)
    y_label= np.vstack((y_label,y1))
    # print(y_label,i,y_label.shape)
print(y_label.shape)