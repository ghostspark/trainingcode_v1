import urllib.request as r
import json
from lxml.html import etree
import xlwt
import time
import re
f=open("20200711-II.json",'w',encoding='utf-8')
job_info={}
headers={
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        }
localtime=time.asctime(time.localtime(time.time()))
for i in range(0,1):
    url='https://www.liepin.com/zhaopin/?compkind=&dqs=250&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=ETL%E5%BC%80%E5%8F%91&siTag=wAxGOaXU9agF7VQpGFbCBw%7EE08QNgJtmOV680BaDaEpHQ&d_sfrom=search_fp&d_ckId=8751774a5e191694b94037a79842ffea&d_curPage='+str(i)+'&d_pageSize=40&d_headId=6e60a7a98f5b580b44c3d2fd885a5b2c&curPage='+str(i+1)
    #https://www.liepin.com/zhaopin/?compkind=&dqs=250&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=ETL%E5%BC%80%E5%8F%91&siTag=wAxGOaXU9agF7VQpGFbCBw%7EE08QNgJtmOV680BaDaEpHQ&d_sfrom=search_fp&d_ckId=8751774a5e191694b94037a79842ffea&d_curPage=0&d_pageSize=40&d_headId=6e60a7a98f5b580b44c3d2fd885a5b2c&curPage=1
    response=r.Request(url=url,headers=headers)
    data=r.urlopen(response).read().decode("utf-8")
    data1=etree.HTML(data)
    
    for j in range(40):
        #data2=data1.xpath("//div[@class='job-info']//a[@target='_blank']/@href".format(j))
        #print(data2)
        #for I in data2:
        try:
            job_title = data1.xpath("//div[@class='job-info']/h3/a/text()")[j]
        except:
            job_title=[]
        try:
            job_title_url=data1.xpath("//div[@class='company-info nohover']/p//a[@target='_blank']/@href")[j]
        except:
            job_title_url=[]
        try:
            job_company = data1.xpath("//div[@class='company-info nohover']/p/a/text()")[j]
        except:
            job_company=[]
        try:
            job_company_url = data1.xpath("//div[@class='company-info nohover']/p//a[@target='_blank']/@href")[j]
        except:
            job_company_url = []
        try:
            job_address = data1.xpath("//div[@class='job-info']/p/a/text()")[j]
        except:
            job_address=[]
        try:
            job_salary = data1.xpath("//div[@class='job-info']/p/span/text()")[j]
        except:
            job_salary=[]
        try:
            job_href = data1.xpath("//div[@class='job-info']/p/time/text()")[j]
        except:
            job_href=[]
        a=''.join(job_salary)
        b=re.findall(r"\d+\.?\d*",a)

        job_info['job_sourse']="5"
        job_info['job_title']=str(job_title)
        if len(job_title_url)==0:
            job_info['job_url']=[]
        else:
            job_info['job_url']=str(job_title_url)
        job_info['job_company']=str(job_company)
        if len(job_company_url)==0:
            job_info['job_company_url']=[]
        else:
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
        print("finish")
