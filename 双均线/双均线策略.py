import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts

#1.爬取某只股票信息并保存
pro = ts.pro_api()
fd = pro.daily(ts_code='600519.SH', start_date='19800101', end_date='20210403')
fd.to_csv('test4.csv')

#1.5读取数据并排序
df = pd.read_csv('茅台数据.csv',index_col='trade_date',parse_dates=['trade_date'])[['open','close','high','low']]
df = df.sort_index(ascending=True)

#2.五日均线与六十日均线
df['ma5'] = np.nan
df['ma60'] = np.nan
for i in range(4,len(df)):
    df.loc[df.index[i],'ma5'] = df.loc[df.index[i-4:i+1],'open'].mean()
for i in range(59,len(df)):
    df.loc[df.index[i],'ma60'] = df.loc[df.index[i-59:i+1],'open'].mean()
# for i in range(4, len(df)):
#     df.loc[df.index[i],'ma5'] = df['close'][i-4:i+1].mean()
#
# for i in range(29, len(df)):
#     df.loc[df.index[i],'ma30'] = df['close'][i-29:i+1].mean()

#3.切前三百画图
df[['close','ma5','ma60']].plot()
plt.show()

#4.金叉和死叉
# df3 = df.dropna()
# df3 = df3['19800101':]
# golden_cross = []
# death_cross = []
# for i in range(1,len(df3)):
#     if df3['ma5'][i-1] < df['ma60'][i-1] and df['ma5'][i] >= df['ma60'][i]:
#         golden_cross.append(df3.index[i])
#     elif df3['ma5'][i-1] > df['ma60'][i-1] and df['ma5'][i] <= df['ma60'][i]:
#         death_cross.append(df3.index[i])

df = df.dropna()
df = df['1980-01-01':]
golden_cross = []
death_cross = []
for i in range(1,len(df)):
    if df['ma5'][i] >= df['ma60'][i] and df['ma5'][i-1] < df['ma60'][i-1]:
        golden_cross.append(df.index[i])
    if df['ma5'][i] <= df['ma60'][i] and df['ma5'][i-1] > df['ma60'][i-1]:
        death_cross.append(df.index[i])

# sr1 = df['ma5'] < df['ma60']
# sr2 = df['ma5'] >= df['ma60']

# death_cross = df[sr1 & sr2.shift(1)].index
# golden_cross = df[~(sr1 | sr2.shift(1))].index

#5.策略收益
sr1 = pd.Series(1,index=golden_cross)
sr2 = pd.Series(0,index=death_cross)
sr = sr1.append(sr2).sort_index()
print('茅台双均线策略（从发行股票第一天开始）')
first_money = 100000
print('本金:',first_money)
money = first_money
hold = 0
for i in range(len(sr)):
    p = df['open'][sr.index[i]]
    if sr.iloc[i]== 1:
        buy = (money // (100*p))
        money -= buy*100*p
        hold += buy*100
    else:
        money += hold*p
        hold = 0
        print(f'第{i//2+1}次交易后的收益：',money-first_money)
p = df['close'][-1]
last_money = p*hold +money


print('总收益:',last_money-first_money)
