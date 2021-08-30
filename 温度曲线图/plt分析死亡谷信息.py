''''''
'''
分析温度
'''

# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt
#
# filename = 'death_valley_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     # for i,v in enumerate(header_row):
#     #     print(f'{i} {v}')
#     highs,lows,dates = [],[],[]
#
#     for row in reader:
#         date = datetime.strptime(row[2], '%Y-%m-%d')
#         try:
#             high = int(row[4])
#             low = int(row[5])
#         except ValueError:
#             print(f'Missing data for {date}')
#         else:
#             highs.append(high)
#             lows.append(low)
#             dates.append(date)
#
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.plot(dates,highs,c='red',alpha=0.5)
# ax.plot(dates,lows,c='blue',alpha=0.5)
# ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#
# # 设置图形格式
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
#
# ax.set_title('2018年每日最高最低温度\n美国加利福尼亚州死亡谷',fontsize=20)
# ax.set_xlabel('',fontsize=16)
# fig.autofmt_xdate() # 设置倾斜
# ax.set_ylabel('温度（F）',fontsize=16)
#
# ax.tick_params(axis='both',which='major',labelsize=16)
# # plt.yticks(range(0,100,10)) # 设置某一个轴的下限，上限和间隔
#
# plt.show()

'''
分析降水量
'''
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'death_valley_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f) # 调用reader函数返回一个阅读器对象
#     header_row = next(reader) # 调用next函数将阅读器对象作为参数传入时，它将返回文件的下一行
#     # for index,col_header in enumerate(header_row):
#     #     print(f'{index} {col_header}')
#
#     # 从文件中获取降水量
#     dates, prcps= [],[]
#     for row in reader:
#         # 获取最高最低温度信息
#         prcp = eval(row[3])
#         prcps.append(prcp)
#         # 获取日期信息
#         date = datetime.strptime(row[2],'%Y-%m-%d')
#         dates.append(date)
#
# # 绘制最高温度图形
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.plot(dates,prcps,c='red',alpha=0.5)
#
# # 设置图形格式
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
#
# ax.set_title('2018年每日降水量',fontsize=24)
# ax.set_xlabel('',fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('降水量',fontsize=16)
#
# ax.tick_params(axis='both',which='major',labelsize=16)
# # plt.yticks(range(0,100,10)) # 设置某一个轴的下限，上限和间隔
#
# plt.show()

'''
对比死亡谷和锡特卡温度信息
要在同一个图表上 呈现两组数据集 可以多次调用ax.plot
'''
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_temp(filename,key="TMAX"):
    with open(filename) as f:
        reader = csv.reader(f)
        dates = []
        highs = []
        # 自动获取索引值
        header_row = next(reader)
        high_index = header_row.index(key)
        date_index = header_row.index("DATE")

        # 获取最高最低温度信息
        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')

            try:
                high = int(row[high_index])
            except ValueError:
                print(f'Missing data for {date}')
            else:
                highs.append(high)
                dates.append(date)
    return highs,dates



filename1 = 'sitka_weather_2018_simple.csv'
filename2 = 'death_valley_2018_simple.csv'

s_highs,s_dates = get_temp(filename1)
d_highs,d_dates = get_temp(filename2)
s_lows,s_dates2 = get_temp(filename1,key="TMIN")
d_lows,d_dates2 = get_temp(filename2,key="TMIN")


# 绘制最高温度图形
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(s_dates,s_highs,c='red',alpha=0.5)
ax.plot(d_dates,d_highs,c='red',alpha=0.5)
ax.plot(s_dates2,s_lows,c='blue',alpha=0.5)
ax.plot(d_dates2,d_lows,c='blue',alpha=0.5)

ax.fill_between(s_dates,s_highs,d_highs,facecolor='red',alpha=0.1)
ax.fill_between(s_dates2,s_lows,d_lows,facecolor='blue',alpha=0.1)

# 设置图形格式
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签

ax.set_title('死亡谷与锡特卡\n2018年每日最高最低气温比较',fontsize=20)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度（F）',fontsize=16)

ax.tick_params(axis='both',which='major',labelsize=16)
# plt.yticks(range(0,100,10)) # 设置某一个轴的下限，上限和间隔
plt.yticks(range(0,150,20))
plt.show()