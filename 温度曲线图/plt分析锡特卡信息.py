''''''
'''
分析温度
'''
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f) # 调用reader函数返回一个阅读器对象
#     header_row = next(reader) # 调用next函数将阅读器对象作为参数传入时，它将返回文件的下一行
#     # for index,col_header in enumerate(header_row):
#     #     print(f'{index} {col_header}')
#
#     # 从文件中获取最高气温
#     dates,highs,lows = [],[],[]
#     for row in reader:
#         # 获取最高最低温度信息
#         high = int(row[5])
#         highs.append(high)
#         low = int(row[6])
#         lows.append(low)
#
#         # 获取日期信息
#         date = datetime.strptime(row[2],'%Y-%m-%d')
#         dates.append(date)
#
#
# # 绘制最高温度图形
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.plot(dates,highs,c='red',alpha=0.5)
# ax.plot(dates,lows,c='blue',alpha=0.5)
# ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#
# # 设置图形格式
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
#
# ax.set_title('2018年每日最高最低温度',fontsize=24)
# ax.set_xlabel('',fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('温度（F）',fontsize=16)
#
# ax.tick_params(axis='both',which='major',labelsize=16)
# # plt.yticks(range(0,100,10)) # 设置某一个轴的下限，上限和间隔
#
# plt.show()

'''
分析降水量
'''
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # 调用reader函数返回一个阅读器对象
    header_row = next(reader) # 调用next函数将阅读器对象作为参数传入时，它将返回文件的下一行
    # for index,col_header in enumerate(header_row):
    #     print(f'{index} {col_header}')

    # 从文件中获取降水量
    dates, prcps= [],[]
    for row in reader:
        # 获取最高最低温度信息
        prcp = eval(row[3])
        prcps.append(prcp)
        # 获取日期信息
        date = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(date)

# 绘制最高温度图形
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,prcps,c='red',alpha=0.5)

# 设置图形格式
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签

ax.set_title('2018年每日降水量',fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('降水量',fontsize=16)

ax.tick_params(axis='both',which='major',labelsize=16)
# plt.yticks(range(0,100,10)) # 设置某一个轴的下限，上限和间隔

plt.show()
