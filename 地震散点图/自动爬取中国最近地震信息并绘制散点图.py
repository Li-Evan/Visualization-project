# import json
# import requests
# from lxml import etree
#
# earthquake_n = []
# earthquake_t = []
# earthquake_location_lat = []
# earthquake_location_lon = []
# earthquake_location = []
# earthquake_url = []
# earthquake_deapth = []
# shuju = []
# geo_lacation = {}
# geo_data = []
# geo_attrs = []
# geo_values = []
#
# url = 'http://www.ceic.ac.cn/daochu/id:1'
# header = {'User-Agent': 'Mozilla/5.0'}
#
# def Get_html(url=url,header=header):
#
#     r = requests.get(url=url, headers=header)
#     print(r.url)
#     if r.status_code == 200:
#         r.encoding = r.apparent_encoding
#         # print(r.text)
#         html = r.text
#     else:
#         print("网页爬取异常")
#         html = "网页爬取异常"
#     return html
#
#
# def Get_data(html):
#     html = etree.HTML(html)
#     trs = html.xpath("//div[@class='title-content']/div[@class='speedquery']/div[@id='speed-search']/table["
#                      "@class='speed-table1']/tr")
#     print(trs)
#     for tr in trs:
#         earthquake_m1 = tr.xpath("./td[1]/text()")
#         earthquake_t1 = tr.xpath("./td[2]/text()")
#         earthquake_location_lat1 = tr.xpath("./td[3]/text()")
#         earthquake_location_lon1 = tr.xpath("./td[4]/text()")
#         earthquake_deapth1 = tr.xpath("./td[5]/text()")
#         earthquake_location1 = tr.xpath("./td[6]/a/text()")
#         earthquake_url1 = tr.xpath("./td[6]/a/@href")
#         print(earthquake_m1, earthquake_t1, earthquake_location_lat1, earthquake_location_lon1, earthquake_deapth1,
#               earthquake_location1, earthquake_url1)
#         try:
#             earthquake_n.append(earthquake_m1[0])
#             earthquake_t.append(earthquake_t1[0])
#             earthquake_location_lat.append(earthquake_location_lat1[0])
#             earthquake_location_lon.append(earthquake_location_lon1[0])
#             earthquake_deapth.append(earthquake_deapth1[0])
#             earthquake_location.append(earthquake_location1[0])
#             earthquake_url.append(earthquake_url1[0])
#
#         except:
#             print("异常")
#     for i in range(0, len(earthquake_n) - 1):
#         shuju.append((earthquake_n[i], earthquake_t[i], earthquake_location_lat[i], earthquake_location_lon[i],
#                       earthquake_deapth[i], earthquake_location[i], earthquake_url[i]))
#     print(shuju)
#
# Get_data(Get_html())


