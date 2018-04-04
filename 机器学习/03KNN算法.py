import math
import csv
import random
import operator


class KNearestNeighbor(object):
    def __init__(self):
        pass

    # 加载数据集  split以某个值为界限分类train和test
    def loadDataset(self, filename, split, trainingSet, testSet):
        with open(filename, "r") as csvfile:
            lines = csv.reader(csvfile)  # 读取所有的行
            dataset = list(lines)  # 转化成列表
            for x in range(len(dataset) - 1):
                for y in range(4):
                    dataset[x][y] = float(dataset[x][y])
                    # 将所有数据加载到train和test中
                if random.random() < split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])

    # 计算距离
    def calculateDistance(self, testData, trainData, length):
        distance = 0  # length表示维度 数据共有几维
        for x in range(length):
            distance += pow((testData[x] - trainData[x]), 2)  # 累加,四个维度的距离
        return math.sqrt(distance)

    # 返回最近的k个边距
    def getNeighbors(self, trainingSet, testInstance, k):
        distance = []
        length = len(testInstance) - 1  # 维度(列),去掉分类标签列
        # 对训练集的每一个数计算其到测试集的实际距离(一条测试数据对所有训练集)
        for x in range(len(trainingSet)):
            dist = self.calculateDistance(testInstance, trainingSet[x], length)
            print('训练集:{}-距离:{}'.format(trainingSet[x], dist))
            distance.append((trainingSet[x], dist))

        # 把距离从小到大排序
        distance.sort(key=operator.itemgetter(1))  # 1代表dist
        # print(distance)
        neighbors = []
        for x in range(k):
            neighbors.append(distance[x][0])
            # print(neighbors)
            return neighbors

    # 根据少数服从多数，决定归类到哪一类
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            # 统计每一个分类的个数
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        # print(classVotes.items())
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    # 准确率计算
    def getAccuracy(self, testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            # predictions是预测的和testset实际的比对
            if testSet[x][-1] == predictions[x]:
                correct += 1
        print('共有{}个预测正确,共有{}个测试数据'.format(correct, len(testSet)))
        return (correct / float(len(testSet))) * 100.0

    def Run(self):
        trianingSet = []
        testSet = []
        split = 0.75
        self.loadDataset(r'testdata.txt', split, trianingSet, testSet)
        print('Train set:' + str(len(trianingSet)))
        print('Test set' + str(len(testSet)))
        predictions = []
        # 取最近的3个数据
        k = 3
        # 对所有的测试集进行测试
        for x in range(len(testSet)):
            neighbors = self.getNeighbors(trianingSet, testSet[x], k)
            # 找这3个邻居归类到哪一类
            result = self.getResponse(neighbors)
            predictions.append(result)

        accuracy = self.getAccuracy(testSet, predictions)
        print('Accuracy:' + repr(accuracy) + '%')

if __name__ == '__main__':
    a = KNearestNeighbor()
    a.Run()
