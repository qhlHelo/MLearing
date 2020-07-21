import numpy as np
import matplotlib.pyplot as plt

# from matplotlib.image import imread

# 生成数据
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='--', label='cos')  # 虚线绘制
plt.xlabel("x")  # x轴
plt.ylabel("y")  # y轴
plt.title('sin & cos')  # 标题
plt.legend()
# img = imread('/xxx/xx.png') # 读入图像
# plt.imshow(img)
plt.show()
