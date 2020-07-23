"""
使用numpy模拟前向传播
"""
import numpy as np

'''
init network
初始化三层网络的w、b
'''


def init_network():
    network = dict()
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network


'''
activation function
使用sigmoid函数
'''


def activation(x):
    return 1 / (1 + np.exp(-x))


'''
output layer
恒等式
'''


def identity(x):
    return x


"""
Forward Propagation
"""


def forward_propagation(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = activation(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = activation(a2)
    a3 = np.dot(z2, W3) + b3
    return identity(a3)


if __name__ == '__main__':
    network = init_network()  # init network, w & b
    x = np.array([1.0, 0.5])  # init network, x
    y = forward_propagation(network, x)  # forward propagation and output
    print(y)
