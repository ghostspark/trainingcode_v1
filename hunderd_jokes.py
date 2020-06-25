import urllib.request as r
import re
from lxml.html import etree
num=input('输入爬取页数')

for a in range(int(num)):
    url='https://www.qiushibaike.com/text/{}/'.format(num)
    response=r.Request(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        })
    data=r.urlopen(response).read().decode('utf-8')
    data2=etree.HTML(data)
    data2=data2.xpath('//div[@class="content"]/span/text()')
    print(data2)

    l=[]
    for i in data2:
        if i=='查看全文':
             continue
        data3=re.findall('\n*(.*?)\n*',i)
        for j in data3:
            l.append(j)
        if len(re.findall('\n',i))==2:
                l.append('\n')
                l.append('\n')
    with open('jokes.txt','a',encoding='utf-8') as f:
        for i in l:
            f.write(i)
        f.close()
