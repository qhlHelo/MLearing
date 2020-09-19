import torch
import numpy as np
import torch.nn as nn

"""
CNN：pytorch测试
"""
image = np.array([[1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1],
                  [0, 0, 1, 1, 0],
                  [0, 1, 1, 0, 0]])

filter_1 = np.array([[1, 0, 1],
                     [0, 1, 0],
                     [1, 0, 1]])

filters = np.array([filter_1])

image = image.astype('float32')

# unsqueeze：升维
image = torch.from_numpy(image).unsqueeze(0).unsqueeze(1)
weight = torch.from_numpy(filters).unsqueeze(1).type(torch.FloatTensor)

# 1输入通道，1输出通道，filter_size=3
conv = nn.Conv2d(1, 1, kernel_size=(3, 3), stride=1, padding=0, bias=False, padding_mode='zeros')
conv.weight = nn.Parameter(weight)
conv_output = conv(image)
print("output: ", conv_output)
