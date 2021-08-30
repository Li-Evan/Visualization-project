import plotly.express as px

# 用于显示所有的渐变配色方案
for key in px.colors.named_colorscales():
    print(key)

# 将对应的颜色的配色列表反转
px.colors.diverging.RdYlGn[::-1]