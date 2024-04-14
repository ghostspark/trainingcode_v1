import requests
import pandas as pd
from pyecharts import Bar, Line, Overlap, Grid

url = 'http://investor.apple.com/feed/SECFiling.svc/GetEdgarFilingList?apiKey=BF185719B0464B3CB809D23926182246&exchange=CIK&symbol=0000320193&formGroupIdList=1%2C4&excludeNoDocuments=true&pageSize=-1&pageNumber=0&tagList=&includeTags=true&year=-1&excludeSelection=1'
rsp = requests.get(url)
data = rsp.json()

# 从文件中搜索相关信息
for y in range(2008, 2018):
    print('\n-------------------', y)
    ex = pd.ExcelFile('data/%d.xls' % y)
    sheets = pd.read_excel(ex, None)
    for sheet in sheets:
        s = sheets[sheet]
        for index, row in s.iterrows():
            line = str(row.values)
            if 'china' in line.lower():
                print(sheet)
                print(line, '\n')

# 转换数据格式
table = table.strip().split('\n')
head = table[0].split()
body = table[1:]
data = {}
year = 2008
for line in body:
    data_year = {}
    line = line.split()
    for i in range(len(head)):
        data_year[head[i]] = line[i]
    data[year] = data_year
    year += 1
data = pd.DataFrame(data)


#制图
years = [str(i) for i in range(2008, 2018)]
net_sales = data.loc['净销售额'].values
net_income = data.loc['净利润'].values
bar = Bar("盈利能力")
bar.add("净销售额", years, net_sales)
bar.add("净利润", years, net_income, bar_category_gap=25, yaxis_name='百万美元', yaxis_name_gap=60)
gross = data.loc['毛利率'].values
line = Line()
line.add("毛利率", years, gross, line_width=3)
ol = Overlap()
ol.add(bar)
ol.add(line, is_add_yaxis=True, yaxis_index=1)

assets = data.loc['总资产'].values
cash = data.loc['现金'].values
bar = Bar("财务状况")
bar.add("总资产", years, assets)
bar.add("现金", years, cash, bar_category_gap=25, yaxis_name='百万美元', yaxis_name_gap=60)
print(bar)
