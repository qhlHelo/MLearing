"""
使用numpy搭建神经网络
Step1.定义网络结构(输入层、隐藏层、输出层)
Step2.初始化模型参数
Step3.循环操作:
    - 执行前向传播，得到prediction
    - 计算损失函数
    - 执行反向传播
    - 权值更新
"""
import numpy as np

'''
init network
初始化三层网络的w、b
'''
def init_network():
    # noinspection PyShadowingNames
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
使用ReLU函数
'''
def activation(m):
    return np.maximum(0, m)


'''
计算Loss
'''
# noinspection PyShadowingNames
def MSE_Loss(y, y_hat):
    return np.mean(np.square(y - y_hat))


'''
output layer
恒等式
'''
# noinspection PyShadowingNames
def identity(x):
    return x


"""
Forward Propagation
"""
# noinspection PyShadowingNames
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
