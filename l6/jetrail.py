#encoding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
train=pd.read_csv('./train.csv')
print(train)
train.Datetime=pd.to_datetime(train.Datetime)
train.index=train.Datetime
print(train)
train.drop(['ID','Datetime'],axis=1,inplace=True)
print(train)
daily_train=train.resample('D').sum()
print(daily_train)
daily_train['ds']=daily_train.index
daily_train['y']=daily_train.Count
daily_train.drop(['Count'],axis=1,inplace=True)
print(daily_train)

from fbprophet import   Prophet
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)
# 预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
print(future)
forecast=m.predict(future)

pd.options.display.max_columns=100

print(forecast)
m.plot(forecast)
plt.show()

'''
陈博士：
以往作业请帮忙批一下，多谢啦~~
另，我们的数据较简单：{no:[1,2,3,4,5,6,7],values:[100,200,213,501,201,234,985]}
想预测下一次8,9,10的values。 用Prophet是否合适(考虑到Prophet可以输出上下限的区间范围)

'''
