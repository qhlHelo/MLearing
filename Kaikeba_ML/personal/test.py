import numpy as np

# from numpy.random import rand

# x = np.random.randn(13, 10)  # 标准正态分布
#
# print(np.mean(x))
# print(np.std(x))


# ReLU的导数
# def ReLU_Deriv(x):
#     return (x > 0) + 0  # +0是将Boolean的True和False转为1和0


# # 不使用seed
# a = rand(5)
# print(a)
# b = rand(5)
# print(b)
#
# # 使用seed
# np.random.seed(2)
# c = rand(5)
# print(c)
# d = rand(5)
# print(d)
#
# # 使用另外的seed
# np.random.seed(4)
# e = rand(5)
# f = rand(5)
# print(e)
# print(f)

# lights = np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]])
# print(lights[0:1])

# data = load_boston()  # 数据加载
# X = data['data']
# n_hidden = 10
# b1 = np.zeros(X.shape[0] * n_hidden).reshape(X.shape[0], n_hidden)
# print(b1)
# print(b1.shape)

"""
Hadamard product && Matrix product
"""
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a * b)  # Hadamard product
print(np.dot(a, b))  # Matrix product
print(np.asmatrix(a) * np.asmatrix(b))  # Matrix product
