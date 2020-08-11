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
