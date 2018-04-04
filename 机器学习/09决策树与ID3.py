from math import log
import operator


# 构造数据
def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 计算信息熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # nrows
    # 为所有分类类目创建字典
    labelCounts = {}
    for featVec in dataSet:
        currentLable = featVec[-1]  # 取得最后一列数据
        if currentLable not in labelCounts.keys():
            labelCounts[currentLable] = 0
        labelCounts[currentLable] += 1
    # 计算香农熵
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 按照最大信息增益划分数据集
# 定义按照某种特征进行划分的函数
# 输入三个变量,待划分的数据集,特征,分类值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet  # 返回不含划分特征的子集


# 定义按照最大信息增益划分数据的函数
def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1  # 特征数量
    baseEntropy = calcShannonEnt(dataSet)  # 香农熵
    bestInforGain = 0  # 信息增益
    bestFeature = -1  # 最优特征的索引值
    for i in range(numFeature):  # 遍历所有特征
        # 获取dataSet的第i个所有特征
        featList = [number[i] for number in dataSet]  # 得到某个特征下(某列)所有值
        uniqualVals = set(featList)  # 无重复的属性特征值
        newEntropy = 0  # 经验条件熵
        for value in uniqualVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))  # 即p(t)
            newEntropy += prob * calcShannonEnt(subDataSet)  # 对各子集香农熵求和
        infoGain = baseEntropy - newEntropy
        # 最大信息增益
        if (infoGain > bestInforGain):
            bestInforGain = infoGain
            bestFeature = i
    return bestFeature  # 返回特征值


# 创建决策树构造函数
# 投票表决
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items, key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # 类别相同,停止划分
    if classList.count(classList[-1]) == len(classList):
        return classList[-1]
    # 长度为1,返回出现次数最多的类别
    if len(classList[0]) == 1:
        return majorityCnt(classList)
    # 按照信息增益最高选取分类特征属性
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 返回分类的特征序号
    bestFeatLable = labels[bestFeat]  # 该特征的label
    myTree = {bestFeatLable: {}}  # 构建数的字典
    del (labels[bestFeat])  # 从labels的list中删除该label
    featValues = [example[bestFeat] for example in dataSet]
    uniqueValues = set(featValues)
    for value in uniqueValues:
        subLabels = labels[:]
        # 构建数据的子集合,并进行递归
        myTree[bestFeatLable][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

# 决策树用于分类
#输入三个变量（决策树，属性特征标签，测试的数据）
def classify(inputTree,featLables,testVec):
    firstStr=list(inputTree.keys())[0] #获取树的第一个特征属性
    secondDict=inputTree[firstStr] #树的分支，子集合Dict
    featIndex=featLables.index(firstStr) #获取决策树第一层在featLables中的位置
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=='dict':
                classLabel=classify(secondDict[key],featLables,testVec)
            else:classLabel=secondDict[key]
    return classLabel


if __name__ == '__main__':
    myDat, labels = createDataSet()
    label = labels.copy()
    # 测试按照特征划分数据集的函数
    # print(splitDataSet(myDat,0,0))
    # print(splitDataSet(myDat,0,1))

    # 测试chooseBestFeatureToSplit函数
    # print(chooseBestFeatureToSplit(myDat))

    # 决策树构造函数测试
    mytree = createTree(myDat, labels)
    print(classify(mytree,label,[1,0]))
    print(classify(mytree,label,[1,1]))

