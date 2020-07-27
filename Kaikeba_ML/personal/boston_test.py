import numpy as np
from sklearn import datasets
from sklearn import preprocessing

"""
测试boston房价数据预处理
"""
boston = datasets.load_boston()

X, y = boston.data, boston.target
print(X.shape)
print(y.shape)
# x_mean = X[:, :3].mean(axis=0)  # 前三个特征的均值
# x_std = X[:, :3].std(axis=0)  # 前三个特征的标准差
#
# print(boston.feature_names)
# print(X)
# print("前三个特征的均值：", x_mean)
# print("前三个特征的标准差：", x_std)
#
# X_ = preprocessing.scale(X[:, :3])  # 数据标准化
# X_mean = X_.mean(axis=0)
# X_std = X_.std(axis=0)
# print("标准化后的均值", X_mean)
# print("标准化后的标准差", X_std)

"""
测试numpy正太分布
"""
# a = np.random.randint(1, 10, size=2)  # 最小值,最大值,数量
# print(a)
# b = np.random.randn(2)  # 数量
# print(b)
# c = np.random.normal(2)  # 数量
# print(c)
# d = np.random.normal(loc=0, scale=1, size=2)  # 均值mean,标准差std,数量
# print(d)
