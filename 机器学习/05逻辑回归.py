import pandas as pd
import pylab as pl
import numpy as np
import statsmodels.api as sm
import copy

'''
数据集中前三列作为预测变量（predictor variables）：
 gpa
 gre 分数
 rank 表示本科生母校的声望
第四列 admit 则是二分类目标变量，它表明考生最终是否被录用
'''
# 加载数据
df = pd.read_csv("http://cdn.powerxing.com/files/lr-binary.csv")
# print(df.head())
df.columns = ["admit", "gre", "gpa", "prestige"]
# print(df.head())
# 统计指标
# print(df.describe())
# 查看每一列的标准差
# print(df.std())
# 频率表，表示 prestige 与 admin 的值相应的数量关系
# print(pd.crosstab(df['admit'],df['prestige'],rownames=['admit']))
# df.hist()
# pl.show()

# 用 get_dummies 来将”prestige”一列虚拟化
# 产生四列的 dataframe，每一列表示四个级别中的一个
dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')
# print(dummy_ranks.head())
# 为逻辑回归创建所需的 data frame
cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.ix[:, 'prestige_2':])
# print(data.head())
# 需要自行添加逻辑回归所需的 intercept 变量,截距=1
data['intercept'] = 1.0
# 生成 m 个虚拟变量后，只要引入 m-1 个虚拟变量到数据集中，未引入的一个是作为基准对比的
# 指定作为训练变量的列，不含目标列`admit
train_cols = data.columns[1:]
# print(train_cols)
logit = sm.Logit(data['admit'], data[train_cols])
result = logit.fit()

# 构建预测集
# 与训练集相似，一般也是通过 pd.read_csv() 读入
# 在这边为方便，我们将训练集拷贝一份作为预测集（不包括 admin 列）

combos = copy.deepcopy(data)
#数据中的列要跟预测时用到的列一致
predict_cols = combos.columns[1:]
# 预测集也要添加 intercept 变量
combos['intercept'] = 1.0
# 进行预测，并将预测评分存入 predict 列中
combos['predict'] = result.predict(combos[predict_cols])

 # 预测完成后， predict 的值是介于 [0, 1] 间的概率值
# 我们可以根据需要，提取预测结果
# 例如，假定 predict > 0.5，则表示会被录取
# 在这边我们检验一下上述选取结果的精确度
total=0
hit=0
for value in combos.values:
    # 预测分数 predict, 是数据中的最后一列
    predict =value[-1]
    #实际录取结果
    admit=int(value[0])
    # 假定预测概率大于 0.5 则表示预测被录取
    if predict>0.5:
        total+=1
        #表示预测命中
        if admit==1:
            hit+=1
#输出结果
print('Total: %d, Hit: %d, Precision: %.2f' % (total, hit, 100.0*hit/total))



