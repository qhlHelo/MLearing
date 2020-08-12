import torch
import numpy as np

# x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(x)
#
# y = torch.zeros(3)
#
# a = np.ones(3)
# z = torch.from_numpy(a)  # numpy转换为torch
# print(z)

'''
截取：narrow(self, dim, start, length)
'''
# i = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(i)
# print(i.narrow(0, 0, 1))
# print(i.narrow(0, 0, 2))
# print(i.narrow(1, 0, 1))
# print(i.narrow(1, 1, 2))

'''
维度转换：view
'''
# a = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = torch.Tensor([[1, 2, 3], [4, 5, 6]])
# # print(a.view(1, 9))
# b = b.view(3, 2)
# print(b.size())

'''
unsqueeze：升维
squeeze：降维
'''
# c = torch.Tensor([[1, 2, 3], [4, 5, 6]])
# print(c, "....", c.size(), c.dim())  # [2,3]
# d = c.unsqueeze(0)
# print(d, "....", d.size(), d.dim())  # [1,2,3]
# e = c.unsqueeze(1)
# print(e, "....", e.size(), e.dim())  # [2,1,3]
# f = d.squeeze(0)
# print(f, "....", f.size(), f.dim())  # [2,3],恢复到c

'''
pow：求幂
'''
# a = torch.Tensor([[1, 2, 3], [4, 5, 6]])
# print(a.pow(-1))
# print(a.pow(2))

'''
sum：求和
'''
# a = torch.Tensor([[1, 2, 3], [4, 5, 6]])
# print(a.sum(dim=0))  # 按列求和
# print(torch.sum(a, 1))  # 按行求和

# print(a.diag_embed())  # 对角矩阵

import torch.nn as nn
import torch.nn.functional as F

'''
对由多个输入平面组成的输入信号进行一维卷积
'''
# F.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)
'''
对由多个输入平面组成的输入图像应用二维卷积
'''
# F.conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)
'''
激活函数
'''
# F.relu(input, inplace=False)
'''
在由多个输入平面组成的输入信号上应用1D 最大池化
'''
# F.max_pool1d(*args, **kwargs)
'''
在由多个输入平面组成的输入信号上应用2D 最大池化
'''
# F.max_pool2d(*args, **kwargs)
'''
在训练过程中, 使用伯努利分布的样本, 随机的用概率p将输入张量的元素归零p，丢掉概率， 默认值为0.5
training，如果 True 使用 dropout，默认为True
inplace，如果设置为 True, 将会原地操作，默认为False
'''
# F.dropout(input, p=0.5, training=True, inplace=False)
