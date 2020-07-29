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
X_ = data['data']
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
X_ = (X_ - np.mean(X_, axis=0)) / np.std(X_, axis=0)

"""
初始化网络参数: 定义隐藏层维度，w1,b1,w2,b2
"""

n_features = X_.shape[1]
n_hidden = 10  # 隐藏层维度
w1 = np.random.randn(n_features, n_hidden)
b1 = np.zeros(n_hidden)
w2 = np.random.randn(n_hidden, 1)
b2 = np.zeros(1)


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
def MSE_loss(y, y_hat):
    return np.mean(np.square(y - y_hat))


# 定义线性回归函数
# noinspection PyShadowingNames
def Linear(X, W, b):
    return np.dot(X, W) + b


# 5000次迭代
for t in range(8000):
    # 前向传播，计算预测值y (Linear -> ReLU -> Linear)
    layer_1_in = Linear(X_, w1, b1)  # 输入到隐藏层
    layer_1_out = ReLU(layer_1_in)  # 第1层输出
    y_hat = Linear(layer_1_out, w2, b2)  # 第2层输出，即预测值
    # 计算损失函数, 并输出每次epoch的loss
    loss = MSE_loss(y, y_hat)
    print("Epoch:", t, "Loss:", loss)
    # 反向传播
    loss_delta = 2 * (y_hat - y)  # 损失函数求导
    # 计算w2梯度
    grad_w2 = np.dot(layer_1_out.T, loss_delta)
    # 计算w1梯度
    # grad_w1 = np.dot(X_, w2.T) * ReLU_Deriv(layer_1_out)
    grad_temp_relu = np.dot(loss_delta, w2.T)
    grad_temp_relu[layer_1_in < 0] = 0
    grad_w1 = np.dot(X_.T, grad_temp_relu)
    # 更新权重, 对w1, w2, b1, b2进行更新
    w1 -= LR * grad_w1
    w2 -= LR * grad_w2
    b1 -= LR * b1
    b2 -= LR * b2

# 得到最终的w1, w2
print('w1={} \n w2={} \n b1={} \n b2={}'.format(w1, w2, b1, b2))
