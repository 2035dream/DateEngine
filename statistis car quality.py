import numpy as np

from pandas import Series, DataFrame
import pandas as pd


pd1 = pd.read_csv('./car_complain.csv')
pd1['brand'] = pd1['brand'].replace('一汽-大众', '一汽大众')
# pd1.to_excel('./car_data_analyze\car_complain.xlsx')
#
pd1 = pd1.drop('problem', axis=1).join(pd1.problem.str.get_dummies(','))
# print(pd1)
tags = pd1.columns[7:]

# 计算每个品牌车型数量
brand_car_count = pd1.groupby(['brand'])['id'].agg(['count'])
brand_car_count['每个品牌车型数量']=brand_car_count['count']
print(brand_car_count)

# 每个车型的不同问题数量
result1 = pd1.groupby(['brand', 'car_model'])[tags].agg(['sum'])
# print(result1)
result1.to_excel('./e1.xlsx')

# 每个车型投诉总数
result1['每个车型投诉总数'] = result1.sum(axis=1)
car_problem_sum = result1
print(car_problem_sum)

result1.to_excel('./e2.xlsx')
#
# 每个品牌投诉总数
brand_pro_sum1 = result1.groupby(['brand']).agg(['sum'])

brand_pro_sum1['每个品牌投诉总数'] = brand_pro_sum1['每个车型投诉总数']
#print(brand_pro_sum1)

# print(brand_pro_sum)

# #打印各品牌平均车型投诉并排序
average_brand=pd.merge(brand_car_count,brand_pro_sum1,left_index=True,right_index=True,how='left')
average_brand['平均车型投诉']=brand_pro_sum1['每个品牌投诉总数'] /brand_car_count['每个品牌车型数量']
print(average_brand)
# print(average_brand)


# def f(x):
#     x = x.replace('一汽-大众', '一汽大众')
#     return x
#
#
# pd1['brand'] = pd1['brand'].replace('一汽-大众', '一汽大众')
# result1 = pd1.groupby(['brand'])['id'].agg(['count'])
# print(result1)
# result2 = pd1.groupby(['brand'])[tag].agg(['sum'])
# print(result2)
# result2.reset_index(inplace=True)
# result2.to_csv('temp1.csv')
