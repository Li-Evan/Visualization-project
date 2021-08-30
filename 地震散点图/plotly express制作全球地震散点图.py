import json
import plotly.express as px
import pandas as pd

'''
提取数据
'''
filename = 'eq_data_30_day_m1.json'
with open(filename,'rt') as f:
    all_eq_data = json.load(f)

# readable_file = 'readable_eq_data.json'
# with open(readable_file,'wt') as f:
#     json.dump(all_eq_data,f,indent=4) # 参数indent=4让json呈现出人看的样子 不然是一整串长长的一条
all_eq_dic = all_eq_data['features']
# print(all_eq_dic)
# print(len(all_eq_dic))

mags,titles,lons,lats = [],[],[],[] # 震级信息，标题，经度，纬度
for each_eq in all_eq_dic:
    mag = each_eq.get('properties').get('mag')
    title = each_eq.get('properties').get('title')
    lon = each_eq.get('geometry').get('coordinates')[0]
    lat = each_eq.get('geometry').get('coordinates')[1]

    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

head_title = all_eq_data.get('metadata').get('title')
# print(mags[:5]) # 小技巧 打印检验的时候不要整个表都打印 打印前面几项就可以了
# print(titles[:5])
# print(lons[:5])
# print(lats[:5])

'''
数据可视化
'''
data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
) # 这种储存相关数据信息的方式(所有信息都以键对值的形式存储)更有利于拓展

# print(data.head()) # 打印头几条信息查看是否正确

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size = '震级',
    size_max=30,
    color='震级',
    color_continuous_scale=px.colors.sequential.Greys,# 用于更改渐变配色方案
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()