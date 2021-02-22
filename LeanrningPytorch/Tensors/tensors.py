import numpy as np
import torch

# <Tensor Initialization>
# Tensors can be initialized in various ways.
'''
Directly from data
'''
data = [[2, 3], [4, 5]]
x_data = torch.tensor(data)
'''
From a NumPy array
'''
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

'''
From another tensor
'''
# x_ones = torch.ones_like(x_data)  # retains the properties of x_data
# x_rand = torch.rand_like(x_data, dtype=torch.float64)  # overrides the datatype of x_data
# print(f"Ones Tensor: \n {x_ones} \n")
# print(f"Rand Tensor: \n {x_rand} \n")

# <Tensor Attributes>
# Tensor attributes describe their shape, datatype, and the device on which they are stored.
# tensor = torch.rand(3, 4)
# print(f"Shape of tensor: {tensor.shape}")
# print(f"Datatype of tensor: {tensor.dtype}")
# print(f"Device tensor is stored on: {tensor.device}")

# <Tensor Operations>
# Over 100 tensor operations, including transposing, indexing, slicing, mathematical operations, linear algebra, random sampling, and more are comprehensively described here.
# Each of them can be run on the GPU (at typically higher speeds than on a CPU). If you’re using Colab, allocate a GPU by going to Edit > Notebook Settings.
tensor = torch.ones(3, 3, dtype=torch.int32)
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
