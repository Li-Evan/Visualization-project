# import random
#
# class RandomWalk:
#
#     def __init__(self,num_point=5000):
#         self.num_points = num_point
#
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         while len(self.x_values) < self.num_points:
#             x_direction = random.choice([1,-1])
#             x_distance = random.choice([0,1,2,3,4])
#             x_step = x_distance * x_direction
#
#             y_direction = random.choice([1, -1])
#             y_distance = random.choice([0, 1, 2, 3, 4])
#             y_step = y_distance * y_direction
#
#             if x_step == 0 and y_step == 0: # 不可以不动
#                 continue
#
#             x = self.x_values[-1] + x_step # x现在的位置是x的最后一个位置加上走的步数
#             y = self.y_values[-1] + y_step # x现在的位置是x的最后一个位置加上走的步数
#
#             self.x_values.append(x)
#             self.y_values.append(y)
#
# import matplotlib.pyplot as plt
# # while True:
# rw = RandomWalk()
# rw.fill_walk()
#
# plt.style.use('seaborn') # 设置样式
# fig,ax = plt.subplots() # 设置画布和图表（必备）,figsize参数设置画布大小(figsize=(15,9))，dpi设置分辨率(dpi=256)
# ax.scatter(
#     rw.x_values,rw.y_values,c=range(rw.num_points),
#     cmap=plt.cm.Blues,s=5,edgecolors='none'
# ) # cmap是颜色映射，可以理解为渐变，具体有哪些样式可以选择可以上matplotlib官网查看！
#
# # 突出起点和终点
# # ax.scatter(0,0,c='green',edgecolors='none',s=100)
# # ax.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolors='none',s=100)
#
# # 隐藏坐标轴
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
#
#
# plt.show()

# import random
#
# class RandomWalk:
#
#     def __init__(self,num_point=5000):
#         self.num_points = num_point
#
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         while len(self.x_values) < self.num_points:
#             x_direction = random.choice([1,-1])
#             x_distance = random.choice([0,1,2,3,4])
#             x_step = x_distance * x_direction
#
#             y_direction = random.choice([1, -1])
#             y_distance = random.choice([0, 1, 2, 3, 4])
#             y_step = y_distance * y_direction
#
#             if x_step == 0 and y_step == 0: # 不可以不动
#                 continue
#
#             x = self.x_values[-1] + x_step # x现在的位置是x的最后一个位置加上走的步数
#             y = self.y_values[-1] + y_step # x现在的位置是x的最后一个位置加上走的步数
#
#             self.x_values.append(x)
#             self.y_values.append(y)
#
# import matplotlib.pyplot as plt
# # while True:
# rw = RandomWalk(5000)
# rw.fill_walk()
#
# plt.style.use('seaborn') # 设置样式
# fig,ax = plt.subplots() # 设置画布和图表（必备）,figsize参数设置画布大小(figsize=(15,9))，dpi设置分辨率(dpi=256)
#
# ax.plot(
#     rw.x_values,rw.y_values,linewidth=1
# ) # cmap是颜色映射，可以理解为渐变，具体有哪些样式可以选择可以上matplotlib官网查看！
#
# # 突出起点和终点
# ax.scatter(0,0,c='green',edgecolors='none',s=100)
# ax.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolors='none',s=100)
#
# # 隐藏坐标轴
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
#
#
# plt.show()
