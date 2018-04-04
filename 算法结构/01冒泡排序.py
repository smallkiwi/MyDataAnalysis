'''
基本思想：
将待排序的元素看做是竖着排列的“气泡”， 较小的元素比较轻， 从而要往上浮
 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该
会是最大的数。
 针对所有的元素重复以上的步骤，除了最后一个。
 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''


def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i + 1]:
                tmp = bubbleList[i]
                bubbleList[i] = bubbleList[i + 1]
                bubbleList[i + 1] = tmp
        listLength -= 1
        print(bubbleList)
    # print(bubbleList)

if __name__ == '__main__':
    l = [2,3,36,52,66,23,89,11]
    bubble(l)
