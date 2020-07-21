import numpy as np
from collections import Counter


def knnModel(trainData, labels, testData, k):
    """
      输入：训练集，训练集标签，测试集，k
      输出：测试集标签
    """
    result = []
    for testData in testData:
        # 计算1条测试数据和所有训练数据坐标的欧式距离：
        dists = [np.sqrt(np.sum((testData - trainData) ** 2)) for trainData in trainData]
        # 或者dists = [np.linalg.norm(testData - trainData) for trainData in trainData]
        # 按距离值从小到大返回对应索引
        indexes = np.argsort(dists)
        # 返回最近的topK标签
        topK = [labels[i] for i in indexes[:k]]
        # 根据标签的数量，最终判定测试集数据的标签结果，并添加到结果中
        result.append(Counter(topK).most_common(1)[0][0])
    return result


if __name__ == '__main__':
    trainData = np.array([[1, 1], [0.4, 5.2], [-2.8, -1.1], [3.2, 1.4], [-1.3, 3.2], [-3, 3.1]])
    labels = [2, 1, 2, 1, 1, 2]
    testData = np.array([[-2.6, 6.6], [1.4, 1.6], [-2.5, 1.2]])
    result = knnModel(trainData, labels, testData, 1)
    print(result)

# 逐一遍历数组
# for i in np.nditer(trainData,order='C'):
#     print(i)

# np.argsort(arr) # 返回数组值从小到大的索引值

# [print() for i in trainData]

# 计算距离
# a = np.array([1,2])
# b = np.array([3,4])
# print(np.sqrt(np.sum(np.square(b-a))))
# print(np.linalg.norm(a-b)) # 等价于上面的

# a = np.array([0, 1, 2])
# print(np.tile(a, (2, 1)))
# print('*' * 8)
# print(np.tile(a, (2, 1, 1)))
# print('*' * 8)
# print(np.tile(a, (2, 2)))
# print('*' * 8)
# print(np.tile(a, (2, 2, 1)))
