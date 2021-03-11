from pandas import Series, DataFrame
import numpy as np

data = {'姓名': ['张飞', '关羽', '刘备', '典韦', '许褚'],
        '语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
print(df1)
print(df1.describe())

df1['总分']=df1.sum(axis=1)
print(df1.sort_values(by='总分'))
print(df1)


