'''
经过 i-1 遍处理后， L[1…i-1]已排好序， 第 i 遍处理仅将 L[i]插入 L[1…i-1]的适当位置， 使得 L[1…i]
又是排好序的序列
算法稳定性与时间复杂度：
算法是稳定的，复杂度为 O(n^2)
'''
def insertSort(DataList):
    for i in range(len(DataList)):
        min_index = i
        for j in range(i+1, len(DataList)):
            if DataList[min_index] > DataList[j]:
                min_index = j
        tmp = DataList[i]
        DataList[i] = DataList[min_index]
        DataList[min_index] = tmp
        print(str(DataList))

if __name__ == '__main__':
    data = [2, 3, 36, 52, 66, 23, 89, 11]
    insertSort(data)