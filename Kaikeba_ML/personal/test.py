# x = np.random.randn(13, 10)  # 标准正态分布
#
# print(np.mean(x))
# print(np.std(x))


# ReLU的导数
def ReLU_Deriv(x):
    return (x > 0) + 0  # +0是将Boolean的True和False转为1和0

