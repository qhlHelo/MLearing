import numpy as np
import torch

'''
<Tensor Initialization>
Tensors can be initialized in various ways.
'''
# Directly from data
# data = [[2, 3], [4, 5]]
# x_data = torch.tensor(data)

# From a NumPy array
# np_array = np.array(data)
# x_np = torch.from_numpy(np_array)

# From another tensor
# x_ones = torch.ones_like(x_data)  # retains the properties of x_data
# x_rand = torch.rand_like(x_data, dtype=torch.float64)  # overrides the datatype of x_data
# print(f"Ones Tensor: \n {x_ones} \n")
# print(f"Rand Tensor: \n {x_rand} \n")

'''
<Tensor Attributes>
Tensor attributes describe their shape, datatype, and the device on which they are stored.
'''
# tensor = torch.rand(3, 4)
# print(f"Shape of tensor: {tensor.shape}")
# print(f"Datatype of tensor: {tensor.dtype}")
# print(f"Device tensor is stored on: {tensor.device}")

'''
<Tensor Operations>
Over 100 tensor operations, including transposing, indexing, slicing, mathematical operations, linear algebra, random sampling, and more are comprehensively described here.
Each of them can be run on the GPU (at typically higher speeds than on a CPU). If you’re using Colab, allocate a GPU by going to Edit > Notebook Settings.
'''
# tensor = torch.ones(3, 3, dtype=torch.int32)
# if torch.cuda.is_available():
#     tensor = tensor.to('cuda')

# Standard numpy-like indexing and slicing
# tensor = torch.ones(4, 5, dtype=torch.int)
# tensor[:, 1] = 0
# print(tensor)

# Sum and Dim
# x = torch.tensor([
#     [[1, 2, 3], [4, 5, 6]],
#     [[1, 2, 3], [4, 5, 6]],
#     [[1, 2, 3], [4, 5, 6]]
# ])
# print(torch.sum(x, dim=0))  # tensor([[3,6,9],[12,15,18]])
# print(torch.sum(x, dim=1))  # tensor([[5,7,9],[5,7,9],[5,7,9]])
# print(torch.sum(x, dim=2))  # tensor([[6,15],[6,15],[6,15]])

# Joining tensors
# You can use torch.cat to concatenate a sequence of tensors along a given dimension. See also torch.stack, another tensor joining op that is subtly different from torch.cat.
# t1 = torch.ones(2, 2, dtype=torch.int)
# t2 = torch.tensor(
#     [[1, 1],
#      [2, 2]]
# )
# t3 = torch.cat([t1, t2], dim=0)
# print(t3)

# Multiplying tensors
# t1 = torch.tensor(
#     [[2, 2],
#      [3, 3]], dtype=torch.int
# )
# t2 = torch.tensor(
#     [[1, 1],
#      [4, 4]], dtype=torch.int
# )
# the element-wise product
# print(f"tensor.mul(tensor)： \n {t1.mul(t2)} \n")
# print(f"tensor * tensor： \n {t1 * t2} \n")
# the matrix multiplication
# print(f"tensor.matmul(tensor)： \n {t1.matmul(t2)} \n")
# print(f"tensor @ tensor)： \n {t1 @ t2} \n")

# In-place operations
# x = torch.tensor([[1, 2], [3, 4], [5, 6]])
# y = torch.rand((3, 2))
# print(y)
# y.copy_(x)
# print(y)


'''
<Bridge with NumPy>
Tensors on the CPU and NumPy arrays can share their underlying memory locations, and changing one will change the other.
'''
# Tensor to NumPy array
# t = torch.ones(5, 5, dtype=torch.int)
# print(f"tensor: {t} \n numpy: {t.numpy()}")
# print(t.add_(2))
# NumPy array to Tensor
n = np.ones(5)
m = torch.from_numpy(n)
print(f"n: {n}\nm: {m}")
np.add(n, 1, out=n)  # Changes in the NumPy array reflects in the tensor.
print(f"n: {n}\nm: {m}")
