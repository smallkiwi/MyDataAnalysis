import random

a = {'a1':4,"a2":6}
b = sorted(a.items(),key=lambda d: d[1], reverse=True)
print(b)
dict = {}
for item in b:
    dict[item[0]] = item[1]
print(dict)

dataSet = [[1,"yes"],[2,"no"]]
classList = [a[-1] for a in dataSet]
print(classList.count(classList[-1]))
print(classList)
print(len(classList[0]))