import numpy as np
import math

# 观测结果
result = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1])
N = len(result)

# 初始化参数
k = 3
# pi,p,q
p = np.array([0.4,0.6,0.7])
Exceptions = np.zeros((N, 1))

for step in range(1000):  # 设置迭代次数
    # E步,计算期望
    for i in range(N):
        # 计算分母
        denominator = p[0] * p[1] ** result[i] * (1 - p[1]) ** (1 - result[i]) + (1 - p[0]) * p[2] ** result[i] * (1 - p[2]) ** (1 - result[i])

        # 分子
        numerator = p[0] * p[1] ** result[i] * (1 - p[1]) ** (1 - result[i])

        Exceptions[i] = numerator / denominator

    oldprob = p.copy()
    p[0] = np.sum(Exceptions) / N
    numerator1 = 0
    numerator2 = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(N):
        numerator1 = numerator1 + Exceptions[i] * result[i]
        denominator1 = denominator1 + Exceptions[i]
        numerator2 = numerator2 + (1 - Exceptions[i]) * result[i]
        denominator2 = denominator2 + (1 - Exceptions[i])

    p[1] = numerator1 / denominator1
    p[2] = numerator2 / denominator2
    # print(p)

    # 判断是否满足要求
    # print(oldprob)
    epsilon = 0.0001
    if np.sum(abs(p - oldprob)) < epsilon:
        print(step)
        print(p)
        break

print("---------------------------------------------------------------------------")
print(p)