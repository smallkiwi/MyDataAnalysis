import numpy as np
import math

# 首先生成一些用于测试的样本
# 指定两个高斯分布的参数，这两个高斯分布的方差相同
sigma = 6
miu_1 = 40
miu_2 = 20

# 随机均匀选择两个高斯分布，用于生成样本值
N = 1000
X = np.zeros((1, N))
for i in range(N):
    if np.random.random() > 0.5:  # 使用的是numpy模块中的random
        X[0, i] = np.random.randn() * sigma + miu_1
    else:
        X[0, i] = np.random.randn() * sigma + miu_2

# 上述步骤已经生成样本
# 对生成的样本，使用EM算法计算其均值miu

# 取miu初始值
k = 2  # 两个正态分布
miu = np.random.random((1, k))
Exceptions = np.zeros((N, k))

for step in range(1000):  # 设置迭代次数
    # 步骤一,E步,计算期望
    for i in range(N):
        # 计算分母
        denominator = 0
        for j in range(k):
            denominator = denominator + math.exp(-1 / (2 * sigma ** 2) * (X[0, i] - miu[0, j]) ** 2)

        # 计算分子
        for j in range(k):
            numerator = math.exp(-1 / (2 * sigma ** 2) * (X[0, i] - miu[0, j]) ** 2)
            Exceptions[i, j] = numerator / denominator

    # 步骤二,M步,求期望的最大
    oldmiu = np.zeros((1, k))
    for j in range(k):
        oldmiu[0, j] = miu[0, j]
        numerator = 0
        denominator = 0
        for i in range(N):
            numerator = numerator + Exceptions[i, j] * X[0, i]
            denominator = denominator + Exceptions[i, j]
        miu[0, j] = numerator / denominator

    # 判断是否满足要求
    epsilon = 0.0001
    if np.sum(abs(miu - oldmiu)) < epsilon:
        break
    print(step)
    print(miu)
print("-----------------------------------------------------------------------")
print('迭代结果:')
print(miu)