"""
使用numpy实现Boston房价预测
Step1 数据加载，来源sklearn中的load_boston
Step2 数据规范化，将X采用正态分布规范化
Step3 初始化网络
Step4 定义激活函数，损失函数，学习率 epoch
Step5 循环执行：前向传播，计算损失函数，反向传播，参数更新
Step6 输出训练好的model参数，即w1, w2, b1, b2
"""
import numpy as np
from sklearn.datasets import load_boston

data = load_boston()  # 数据加载
X = data['data']
y = data['target']

"""
Feature: 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
    CRIM 城镇人均犯罪率
    ZN 住宅用地比例
    INDUS 非零售商业用地比例
    CHAS CHAS变量，0或者1
    NOX 一氧化氮浓度
    RM 每个住宅的平均房间数
    AGE 1940年以前自用房屋的比例
    DIS 距离五个波士顿就业中心的加权距离
    RAD 距离高速公路的便捷指数
    TAX 该地区每一万美元的不动产税率
    PRTATIO 该地区教师学生比例
    B 该地区黑人比例
    LSTAT 该地区中低收入阶层比例
"""

# 将y转化为矩阵的形式
y = y.reshape(y.shape[0], 1)

# 数据规范化
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

"""
初始化网络参数: 定义隐藏层维度，w1,b1,w2,b2
"""

n_features = X.shape[1]
n_hidden = 10  # 隐藏层维度
w1 = np.random.randn(n_features, n_hidden)
b1 = np.zeros(X.shape[0] * n_hidden).reshape(X.shape[0], n_hidden)
w2 = np.random.randn(n_hidden, 1)
b2 = np.zeros(X.shape[0]).reshape(X.shape[0], 1)


# ReLU
def ReLU(x):
    return np.maximum(0, x)


# ReLU导数
def ReLU_Deriv(x):
    return (x > 0) + 0


# 设置学习率
LR = 1e-6


# 定义损失函数
# noinspection PyShadowingNames
def MSE_Lose(y, y_hat):
    return np.mean(np.square(y - y_hat))


# 定义线性回归函数
# noinspection PyShadowingNames
def Linear(X, W, b):
    return np.dot(X, W) + b


# 50000次迭代
for i in range(50000):
    # 1，前向传播，计算预测值y_hat (Linear -> ReLU -> Linear)
    z1 = Linear(X, w1, b1)  # 输入到隐藏层  (506,10)
    a1 = ReLU(z1)  # 第1层输出  (506,10)
    y_hat = Linear(a1, w2, b2)  # 第2层输出，即预测值  (506,1)
    # 计算损失/代价函数, 并输出每次epoch的C
    C = MSE_Lose(y, y_hat)
    print("Epoch:", i, "Cost:", C)

    # 2，反向传播
    delta_L = y_hat - y  # 输出层误差，δL  (506,1)
    grad_w2 = np.dot(a1.T, delta_L)  # 计算w2梯度，δC/δw2  (10,1)
    grad_b2 = delta_L  # 计算b2梯度  (506,1)
    delta_1 = np.dot(delta_L, w2.T) * ReLU_Deriv(a1)  # 计算第1层误差  (506,10)
    grad_w1 = np.dot(X.T, delta_1)  # 计算w1梯度  (13,10)
    grad_b1 = delta_1  # 计算b1梯度  (506,10)

    # 3，更新权重, 对w1, w2, b1, b2进行更新
    w1 -= LR * grad_w1
    w2 -= LR * grad_w2
    b1 -= LR * grad_b1
    b2 -= LR * grad_b2

# 得到最终的w1, w2
print('w1={} \n w2={}'.format(w1, w2))
