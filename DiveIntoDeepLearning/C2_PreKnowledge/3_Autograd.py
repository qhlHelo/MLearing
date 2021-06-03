import torch
'''
若requires_grad = True，则可以追踪其上的所有操作，也可以调用.backward()完成梯度计算，梯度将累积到.grad属性中。
若不想追踪，可调用.detach()将其与追踪记录分离；也可以用with  torch.no_grad()包裹不想被追踪的代码。
每个Tensor都有一个.grad_fn属性，记录tensor的相关运算，若tensor是由运算得到的，则grad_fn返回一个与运算相关的对象，否则是None。
'''

device = torch.device("cuda")  # GPU

# 2.3.2 Tensor
x = torch.ones(2, 2, requires_grad=True, device=device)
# print(f"x: {x}\ngrad_fn: {x.grad_fn}")
y = x + 2
# print(f"y: {y}\ny.grad_fn: {y.grad_fn}")  # x直接创建，所以没有grad_fn，称为叶子节点，对应的grad_fn为None
# print(x.is_leaf, y.is_leaf)
z = y * y * 3  # grad_fn=<MulBackward0>
out = z.mean()  # grad_fn=<MeanBackward0>
print("x:", x, "\nout:", out)

a = torch.randn(2, 2)  # 默认情况下，requires_grad 为 False
a = ((a * 3) / (a - 1))
print(a.requires_grad)  # False
a.requires_grad_(True)
print(a.requires_grad)  # True
b = (a * a).sum()
print(b.grad_fn)  # <SumBackward0>

out.backward()  # 完成out的梯度计算
print("x.grad:", x.grad)  # out关于x的梯度

out2 = x.sum()
out2.backward()  # 再一次反向传播
print(x.grad)  # grad累加

out3 = x.sum()
x.grad.data.zero_()  # 梯度清零
out3.backward()  # 反向传播
print(x.grad)
