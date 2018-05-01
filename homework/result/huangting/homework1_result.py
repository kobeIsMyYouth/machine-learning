# -*- coding: utf-8 -*-
# @Time    : 5/1/18 13:41
# @Author  : huangting
# @FileName: homework1_result.py
# @Software: PyCharm
import numpy as np
from math import sqrt


class Normal(object):

    def min_max_normal(self, arr):
        """
        最大最小值归一化
        :param arr: 需要归一化的矩阵
        :return:
        """
        # B = np.full(shape=A.shape, fill_value=0.0, dtype=float)
        arr = np.array(arr, dtype=float)  # 确保传进来的矩阵是np里面的矩阵
        if arr.shape[0] == 0:
            print("传入的矩阵不能为空！")
        else:
            for i in range(arr.shape[1]):
                _min = np.min(arr[:, i])  # 求该列的最小值
                _max = np.max(arr[:, i])  # 求该列的最大值
                delta = _max - _min
                arr[:, i] = (arr[:, i] - _min) / delta
        return arr

    def zero_mean_normal(self, arr):
        """
        标准差标准化
        :param arr: 需要标准化的矩阵
        :return:
        """
        arr = np.array(arr, dtype=float)  # 确保传进来的矩阵是np里面的矩阵
        if arr.shape[0] == 0:
            print("传入的矩阵不能为空！")
        else:
            for i in range(arr.shape[1]):
                mean = np.mean(arr[:, i])  # 求该列的均值
                var = np.var(arr[:, i])  # 求该列的方差
                for j in range(arr.shape[0]):
                    arr[j, i] = (arr[j, i] - mean) / sqrt(var)
        return arr
