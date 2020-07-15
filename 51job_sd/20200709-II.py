import urllib.request as r
import json
from lxml.html import etree
import xlwt
import time
import re
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
f=open('20200709-II.json','w',encoding='gbk')
localtime=time.asctime(time.localtime(time.time()))
for i in range(1,19):
    url='https://search.51job.com/list/120000,000000,7501%252C7201%252C7503%252C0121%252C0130,00,2,99,%2B,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i)
    response=r.Request(url=url,headers=headers)
    data=r.urlopen(response).read().decode("gbk")
    data1=etree.HTML(data)
    
    for j in range(52):
        data2=data1.xpath('//*[@id="resultList"]/div[{}]'.format(j))
        #print(data2)
        for I in data2:
            job_title = I.xpath('.//p/span/a/text()')
            job_title_url=I.xpath('.//p/span/a/@href')
            job_company = I.xpath('.//span[1]/a/text()')
            job_company_url = I.xpath('.//span[1]/a/@href')
            job_address = I.xpath('.//span[2]/text()')
            job_salary = I.xpath('.//span[3]/text()')
            job_href = I.xpath('.//span[4]/text()')
            a=''.join(job_salary)
            b=re.findall(r"\d+\.?\d*",a)
            #print(len(b))
            #print(b)
            #print(job_title_url)
            #print(job_company_url)

            job_info={}
            job_info['job_sourse']="2"
            job_info['job_title']=str(job_title)
            job_info['job_url']=str(job_title_url)
            job_info['job_company']=str(job_company)
            job_info['job_company_url']=str(job_company_url)
            job_info['job_location']=str(job_address)
            job_info['job_salary']=job_salary
            if len(b)>1:
                job_info['job_max_salary']=eval(b[1])*1000
                job_info['job_min_salary']=eval(b[0])*1000
            else:
                job_info['job_max_salary']=[]
                job_info['job_min_salary']=[]
            job_info['job_release_data']=job_href
            job_info['job_collect_data']=localtime

            print(job_info)

            json.dump(job_info,f,ensure_ascii=False)
            print("fnish")
