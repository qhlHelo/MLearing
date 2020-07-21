import numpy as np
import matplotlib.pylab as plt


#  感知机：b为偏置，w1和w2为权重
#  y = 0 (b + w1x1 + w2x2 <= 0)
#  y = 1 (b + w1x1 + w2x2 > 0)

#  与门
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


#  与门2
def AND2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 阶跃函数1
def step_func1(x):
    y = x > 0
    return y.astype(np.int)  # astype()方法转换NumPy数组的类型


# 阶跃函数2
def step_func2(x):
    return np.array(x > 0, dtype=np.int)


# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    # 与门
    # print(AND(0, 0))
    # print(AND(1, 0))
    # print(AND2(0, 1))
    # print(AND2(1, 1))
    # 感知机
    # x = np.array([0, 1])  # 输入
    # w = np.array([0.5, 0.5])  # 权重
    # b = -0.7  # 偏置
    # print("x=", w * x)
    # print(np.sum(w * x))
    # y = np.sum(w * x) + b
    # print("y=", y)
    # 阶跃函数1
    # y = step_func1(np.array([-1.0, 1.0, 2.0]))
    # print(y)
    # 阶跃函数2及作图
    # x = np.arange(-5.0, 5.0, 0.1)
    # y = step_func2(x)
    # plt.plot(x, y)
    # plt.ylim(-0.1, 1.1)  # 指定y轴的范
    # plt.show()
    # sigmoid函数及作图
    # x = np.arange(-5.0, 5.0, 0.1)
    # y = sigmoid(x)
    # plt.plot(x, y)
    # plt.ylim(-0.1, 1.1)  # 指定y轴的范围
    # plt.show()
    # 矩阵乘积
    # A = np.array([[1, 2], [3, 4]])
    # B = np.array([[5, 6], [7, 8]])
    # x = np.dot(A, B)  # 点乘
    # print(x)
    A = np.array([[1, 2], [3, 4], [5, 6]])
    B = np.array([7, 8])
    x = np.dot(A, B)
    print(x)
    print(B.shape)
