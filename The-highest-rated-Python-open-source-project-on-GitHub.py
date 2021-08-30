import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url=url,headers=headers)
print(f'status code:{r.status_code}')
response_dict = r.json()
print(f'total repositories:{response_dict["total_count"]}')
repo_dicts = response_dict['items']
print(f"repositories returned:{len(repo_dicts)}")

repo_links,stars,labels = [],[],[]

for repo_dict in repo_dicts:

    repo_url = repo_dict['html_url']
    repo_name = repo_dict['name']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)



data = [{
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title':'github上最受欢迎的python项目',
    'xaxis':{'title':'repository'},
    'yaxis':{'title':'stars'},

}

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
# 研究仓库

# print("\nselected information about each repository:")
# for repo_dict in repo_dicts:
#     print(f"name:{repo_dict['name']}")
#     print(f"owner:{repo_dict['owner']['login']}")
#     print(f"stars:{repo_dict['stargazers_count']}") # star数
#     print(f"repository:{repo_dict['html_url']}") # 仓库地址
#     print(f"created:{repo_dict['created_at']}") # 仓库创建时间
#     print(f"updated:{repo_dict['updated_at']}") # 仓库更新时间
#     print(f"description:{repo_dict['description']}") # 仓库描述


    # print('\n')


