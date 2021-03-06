import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from efficient_apriori import apriori

# header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 
# shape为(7501,20)
print(dataset.shape)

# 将数据存放到transactions中
transactions = []
for i in range(0, dataset.shape[0]):               # 按照行进行遍历
    temp = []
    for j in range(0, dataset.shape[1]):                         # 按照列进行遍历  for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
#print(transactions)
# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.03,  min_confidence=0.4)
print("频繁项集：", itemsets)
print("关联规则：", rules)

# 陈博士，
# 请问从关联规则得出以下结论是否正确：
# 1 买牛肉的人，有大于40%的概率会去买矿泉水。
# 2 买牛肉与买矿泉水组合出现的概率大于3%
#
# 关于天池的那道题：
# 是否可以把训练集切片30%，作为测试集。那么就知道预测效果好不好了（因为天池最多只能递交5次）
