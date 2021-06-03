import torch

''' 入门 '''
x = torch.arange(12)
x.shape
x.numel()
y = x.reshape(3, 4)
torch.zeros((2, 3, 4))
torch.ones((2, 3, 4))
torch.randn(3, 4)
torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

''' 运算 '''
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
x + y, x - y, x * y, x / y, x ** y  # **运算符是求幂运算
torch.exp(x)  # e ** x
X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)  # dim=0为行堆叠，dim=1为列堆叠
X == Y
X.sum()

''' 广播机制 '''
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
a + b

''' 索引和切片 '''
X[-1], X[1:3]
X[1, 2] = 9
X[0:2, :] = 12

''' 节省内存 '''
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
l1 = id(x)
x += y  # x地址不变
x[:] = x + y  # x地址不变
x = x + y  # x地址改变，新赋值内存地址

''' 转换为其他Python对象 '''
A = X.numpy()
B = torch.tensor(A)
type(A), type(B)
a = torch.tensor([3.5])
a, a.item(), float(a), int(a)
