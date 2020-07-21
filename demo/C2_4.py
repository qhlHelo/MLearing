# print(dir(np))

# sorted(iterable, *, key=None, reverse=False)
# x = [3, 6, 13, 5, 88, 21, 0]
# y = sorted(x)
# # 默认为升序排序
# print(y)
# # 降序
# print(sorted(x, reverse=True))
# print(list(reversed(y)))
# x = ['a', 'B', 'Haha', 'c', 'D']
# print(sorted(x))
# print(sorted(x, key=str.upper))
# y = [('a', 'helo', 11), ('b', 'Herry', 21), ('c', 'Tom', 8)]
# print(sorted(y, key=lambda i: i[2], reverse=True))


# import random
# print(random.randint(0, 10))
# import datetime
import time
# from datetime import datetime as d
# print(d.now())
# print(datetime.datetime.now())
# for i in range(0, 5):
#     print(i)
#     time.sleep(2)
# 对比for循环和列表解析的效率
# array = []
# start = time.process_time()  # 当前时间
# for i in range(2000000):
#     array.append(i)
# end = time.process_time()
# print(f'for循环消耗的时间是：{end - start}')
#
# start = time.process_time()  # 当前时间
# [i for i in range(2000000)]
# end = time.process_time()
# print(f'列表解析消耗的时间是：{end - start}')

#
# import os
# print(os.getcwd())
# print(os.listdir('.'))
# print(os.listdir())


# import platform
# print(platform.architecture())


import random
# x = ['a', 2, 'c', 'd', 4]
# print(random.choice(x))
# random.choices(population,weights=None,*,cum_weights=None,k=1)
# 其中，population为集群，weights为权重，cum_weights为累加权重，k为选取次数
# print(random.choices(x, weights=[1, 2, 3, 4, 5], k=5))
# print(random.choices(x, weights=[0, 0, 0, 0, 0], k=5))
# print(random.choices(x, weights=[1, 1, 1, 1, 1], k=5))
# print(random.choices(x, cum_weights=[0, 0, 0, 0, 0], k=5))
# print(random.choices(x, cum_weights=[1, 1, 1, 1, 1], k=5))


# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print("数组为：\n", a)
# print("*" * 10)
# max_ind = np.argmax(a, axis=0)  # 沿第一个轴找最大值的索引
# print(max_ind)
# print(dir(np))
# print(np.version.version)
# print("维度：", a.ndim)
# print("各维度的长度：", a.shape)
# print("元素总数：", a.size)
# print("元素类型：", a.dtype)

# b = np.arange(0, 20, 5)  # arange(开始值，终值，步长)
# print(b)
# print(b.reshape(2, 2))  # 改变数组形状
# c = np.linspace(0, 2, 10)  # linspace(开始值，终值，元素个数)
# print(c)
# zero_arr = np.zeros((3,4))   # 快速创建元素全为0的数组
# print(zero_arr)
# one_arr = np.ones((2, 3, 4), dtype=np.int64)  # 快速创建元素全为1的数组，并将类型设置为整型
# print(one_arr)
# eye = np.eye(3, dtype=int)
# print(eye)
# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr[0:4])
# print(arr[0:4:2])  # (开始:结束:步长)
# arr = arr.reshape(2, 3)
# print(arr)
# print(arr[0, :])
# print(arr[0, 1])
# print(arr[:, 1])
# arr1 = np.array([[1, 2], [3, 4]])  # 声明两个二维数组
# print(arr1)
# print("********")
# arr2 = np.array([[5, 6], [7, 8]])
# print(arr2)
# print(arr2-arr1)
# print(arr2+arr1)
# print(arr2*arr1)
# print(arr2/arr1)
# print(arr1**2)
# print(arr1 @ arr2)  # 矩阵乘积
# print("*" * 10)
# print(np.dot(arr1, arr2))  # 矩阵乘积
# print("*" * 10)
# print(arr1.dot(arr2))  # 矩阵乘积
# print(arr1.T)
# arr3 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr3)
# print("arr3中最大元素的索引为: ", np.argmax(arr3))  # 数组中值最大元素的索引
# print("arr3中沿第一个轴最大元素的索引为: ", np.argmax(arr3, axis=0))  # 数组中沿第一个维度值最大元素的索引，0代表列
# print("arr3中沿第二个轴最大元素的索引为: ", np.argmax(arr3, axis=1))  # 数组中沿第二个维度值最大元素的索引，1代表行


import random

x = ['快递太慢了！', '不好吃', '特别难吃', '要齁死我了', '很划算', '下次还来', '味道很不错！', '香']
y = ['差评', '差评', '差评', '差评', '好评', '好评', '好评', '好评']


def shuffle(x, y):
    z = list(zip(x, y))
    random.shuffle(z)
    x, y = zip(*z)
    return x, y


# def shuffle(x, y):
#     """
#     输入2个数据集，保证数据和标签的对应关系，（不改变原始数据）输出数据集打乱后的结果
#     parameters:
#         x: 数据集1
#         y: 数据集2
#     return:
#         返回元组(z1,z2)
#         z1: 乱序后的数据集1
#         z2: 乱序后的数据集2
#     """
#     # 记录x的索引
#     index = [i for i in range(len(x))]
#     # 生成字典，映射原始数据集x
#     tmp = dict(zip(x, index))
#     # 记录原始数据集x的索引对应关系，打乱数据集x后，根据新数据集x获取索引后，生成对应的新数据集y
#     # 打乱数据集x
#     z1 = random.sample(x, k=len(x))
#     # 从z1逐一取值，从字典tmp查询
#     z2 = [y[tmp.get(i)] for i in z1]
#     return z1, z2
#
#
if __name__ == '__main__':
    # 原始对应关系为
    print("----原始对应关系----")
    [print(i, ':', j) for i, j in zip(x, y)]
    # 打乱排序后的结果为
    print("----乱序后的结果----")
    z = shuffle(x, y)
    [print(i, ':', j) for i, j in zip(z[0], z[1])]

# from collections import Counter
#
# text = '2019 年 十月 一日 上午 ， 庆祝 中华人民共和国 成立 70 周年 阅兵式 在 首都北京 盛大举行 ， 59 个 阅兵 方阵 ， 580 台受 阅 装备 ， 1.5 万人 的 参阅 队伍 接受 了 全国 人民 ' \
#        '的 检阅 。 阅兵 装备 方队 展示 的 武器装备 皆 为 国产 现役 主战 装备 ， 40% 为 首次 展示 。 其中 近些年来 广受 全球 关注 的 东风 41 洲际 弹道导弹 ， 巨浪 二潜射 弹道导弹 ， 东风 ' \
#        '17 高超音速 武器 系统 终于 揭幕 亮剑 ， 以 " 不怒 自威 " 的 形象 向 世界 展示 中国 捍卫 和平 的 意志 与 力量 。 相较 于 其他 首度 公开 亮相 的 武器装备 ， 这 三款 武器 多年 来 ' \
#        '传闻 不断 ， 备受 关注 ， 并 因 其 " 大国 基石 " 的 地位 而 被 公众 赋予 特殊 的 期待 ， 这 三款 武器装备 实力 究竟 如何 ， 又 各自 承担 着 怎样 的 历史 " 使命 " 呢 ？ 本报 ' \
#        '特约 相关 领域 军事 专家 ， 为 大家 详细 解读 这 三款 彰显 国威 ， 震撼 世界 的 国 之 重器 。 '
#
#
# def count_words(text):
#     x = Counter(text.split(' '))
#     return str(x)[8:-1]  # 原始数据用Counter包起来，字符串截取后，统计数据降序输出
#     # return dict(x.items())  # 正常返回的字典数据，不美观
#
#
# print(count_words(text))
