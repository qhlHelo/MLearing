import torch

"""
2.1 创建Tensor
"""
# x = torch.empty(5, 3)
# print("x: ", x)
# x = torch.rand(5, 3)
# print("x: ", x)
# x = torch.zeros(5, 3, dtype=torch.long)
# print("x: ", x)
x = torch.tensor([5.5, 3])
print("x: ", x)
print("dtype:", x.dtype, "\t", "device:", x.device)
x = x.new_ones(5, 3, dtype=torch.float64)  # 返回的tensor默认具有相同的torch.dtype和torch.device
print("x: ", x)
x = torch.randn_like(x, dtype=torch.float)  # 指定新的数据类型
print("x: ", x, "\n", x.size(), x.shape)
# print("x.size: ", x.size())  # 返回的torch.Size其实就是一个tuple, 支持所有tuple的操作
# print("x.shape: ", x.shape)
'''
Tensor(*sizes)	基础构造函数
tensor(data,)	类似np.array的构造函数
ones(*sizes)	全1Tensor
zeros(*sizes)	全0Tensor
eye(*sizes)	对角线为1，其他为0
arange(s,e,step)	从s到e，步长为step
linspace(s,e,steps)	从s到e，均匀切分成steps份
rand/randn(*sizes)	均匀/标准分布
normal(mean,std)/uniform(from,to)	正态分布/均匀分布
randperm(m)	随机排列
'''

"""
2.2 操作
"""
'''
A.算术操作
'''
# x = torch.rand(5, 3)
# y = torch.rand(5, 3)
# print("x: ", x)
# print("y: ", y)
# # 加法形式1: +
# print("加法形式1: ", x + y)
# # 加法形式2: add
# print("加法形式2: ", torch.add(x, y))
# # 指定输出
# result = torch.empty(5, 3)
# torch.add(x, y, out=result)  # (input, value, out) # result = input + value
# print("指定输出: ", result)
# # 加法形式3: inplace
# print("加法形式3: ", y.add_(x))


'''
B.索引: 索引出来的结果与原数据共享内存
注意：索引操作不会开辟新内存
'''
# x = torch.rand(5, 3)
# y = x[0, :]  # 取x的第1行所有元素
# print("x: ", x)
# print("y: ", y)
# y += 1
# print("y+1: ", y)
# print(x[0, :])  # 与原数据共享内存，所以内容也被修改
'''
函数	                        功能
index_select(input, dim, index)	在指定维度dim上选取，比如选取某些行、某些列
masked_select(input, mask)	    例子如上，a[a>0]，使用ByteTensor进行选取
nonzero(input)	                非0元素的下标
gather(input, dim, index)	    根据index，在dim维度上选取数据，输出的size与index一样
'''

'''
C.改变形状
view/reshape/clone
'''
x = torch.rand(5, 3)
# print("x: ", x)
# y = x.view(15)
# z = x.view(-1, 5)
# print("y: ", y)
# print("z: ", z)
# y += 1
# print("x: ", x)  # 与原数据共享内存，所以内容也被修改
# print("z: ", z)  # 与原数据共享内存，所以内容也被修改
'''
返回真正的副本，不用共享数据
可以使用reshape()，但此函数并不能保证返回的是其拷贝，不推荐
推荐使用clone创建副本，再view
使用clone的另一个好处：会被记录在计算图中，即梯度回传到副本时也会传到源Tensor
'''
# x_cp = x.clone().view(15)
# print("x: ", x)
# x -= 1
# print("x-1: ", x)
# print("x_cp: ", x_cp)  # 内容没变
'''
item(): 可以将一个标量Tensor转换成一个Python number
'''
# y = torch.randn(1)
# print("y: ", y)
# print("y.item: ", y.item())
'''
线性代数
函数	                            功能
trace	                            对角线元素之和(矩阵的迹)
diag	                            对角线元素
triu/tril	                        矩阵的上三角/下三角，可指定偏移量
mm/bmm	                            矩阵乘法，batch的矩阵乘法
addmm/addbmm/addmv/addr/baddbmm..	矩阵运算
t	                                转置
dot/cross	                        内积/外积
inverse	                            求逆矩阵
svd	                                奇异值分解
'''

"""
2.3 广播机制
"""
# x = torch.arange(1, 3).view(1, 2)
# print("x: ", x)
# y = torch.arange(1, 4).view(3, 1)
# print("y: ", y)
# print("x+y: ", x + y)


"""
2.4 运算的内存开销
python id(): 返回对象的内存地址
"""
# 开辟新的内存地址
# x = torch.tensor([1, 2])
# y = torch.tensor([3, 4])
# id_before = id(y)
# print("id_before: ", id_before)
# y = y + x
# print("id(y): ", id(y))
# print("未使用索引，内存地址是否相同: ", id(y) == id_before)  # False
# 使用索引，指定原来的内存地址
# x = torch.tensor([1, 2])
# y = torch.tensor([3, 4])
# id_before = id(y)
# y[:] = y + x
# print("使用索引，内存地址是否相同: ", id(y) == id_before)  # True
# 使用add(input, value, out)也可以实现
# x = torch.tensor([1, 2])
# y = torch.tensor([3, 4])
# id_before = id(y)
# torch.add(x, y, out=y)  # y += x, y.add_(x)
# print(id(y) == id_before)  # True

"""
2.5 Tensor和NumPy相互转换
"""

"""
2.6 Tensor on GPU
"""
# 以下代码只有在PyTorch GPU版本上才会执行
# if torch.cuda.is_available():
#     device = torch.device("cuda")          # GPU
#     y = torch.ones_like(x, device=device)  # 直接创建一个在GPU上的Tensor
#     x = x.to(device)                       # 等价于 .to("cuda")
#     z = x + y
#     print(z)
#     print(z.to("cpu", torch.double))       # to()还可以同时更改数据类型
