import urllib.request as r
import os
#爬取天气数据
b=input("请输入城市（拼音）：")
url='http://api.openweathermap.org/data/2.5/forecast?q='+b+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'    

data=r.urlopen(url).read().decode('utf-8')
import json
import numpy as np
import matplotlib.pyplot as plt
data=json.loads(data)
#未来5天天气
for i in range(5):
    print("第{}天:".format(i+1))
    print("  当天的温度是----------"+str(data['list'][i]['main']['temp']))
    print("  当天的最低温度是------"+str(data['list'][i]['main']['temp_min']))
    print("  当天的最高温度是------"+str(data['list'][i]['main']['temp_max']))
    print("  当天气压为------------"+str(data['list'][i]['main']['pressure']))
    print("  当天体感温度----------"+str(data['list'][i]['main']['feels_like']))
    print("·时间："+str(data['list'][i]['dt_txt']))
    print("=================================================================")
#存储.json
a=json.dumps(data)
f2=open('yuanchuan.json','w')
f2.write(a)
f2.close
