import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
'''
1.K-means算法的基本思想是：
以空间中k个点为中心进行聚类，
对最靠近他们的对象归类。通过迭代的方法，
逐次更新各聚类中心的值，直至得到最好的聚类结果。

2. 算法大致流程为：

1）随机选取k个点作为种子点(这k个点不一定属于数据集)

2）分别计算每个数据点到k个种子点的距离，离哪个种子点最近，就属于哪类

3）重新计算k个种子点的坐标(简单常用的方法是求坐标值的平均值作为新的坐标值)

4）重复2、3步，直到种子点坐标不变或者循环次数完成
'''
# 读取数据
X = []
f = open('city.txt')
for v in f:
    X.append([float(v.split(',')[1]), float(v.split(',')[2])])
# 转换成numpy array
X = np.array(X)
# 类簇的数量
n_clusters = 5
# 聚类
cls = KMeans(n_clusters).fit(X)
# X中每项所属分类的一个列表
# print(cls.labels_)
# 画图
markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members,0],X[members,1],s=60,marker=markers[i],c='b',alpha=0.5)
plt.show()
