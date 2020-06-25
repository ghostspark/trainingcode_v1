import urllib.request as r
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
#温度排序+平均温度
list1=[data['list'][0]['main']['temp'],data['list'][1]['main']['temp'],data['list'][2]['main']['temp'],data['list'][3]['main']['temp'],data['list'][4]['main']['temp']]
def paixu():
    list2=sorted(list1)
    print("==============温度排序=============")
    print(list2)
    print("未来5天中最高日气温是"+str(list2[0])+";")
    print("未来5天中最低日气温是"+str(list2[4])+".")
    w=sum(data['list'][0]['main']['temp'],data['list'][1]['main']['temp'],data['list'][2]['main']['temp'],data['list'][3]['main']['temp'],data['list'][4]['main']['temp'])
    ave=w/5
    print("未来5天平均温度为",format(ave))
#字符串图
def tu():
    print('-'*(8*len(list1)-4))
    for j in range(int(max(list1))+1):
        for l in range(len(list1)):
            if j<(max(list1)-list1[l]):
                print(''*4,end='')
            else:
                print('/'*4,end='')
            print(' '*4,end='')
        print()
    print("today"+' '*3,end='')
    if len(list1)>1:
        for m in range(len(list1)):
            print("未来{}天".format(str(m+1)),end='')
    print()
    for n in range(len(list1)):
        print(str(round(list1[n],2))+' '*3,end='')
    print()
    print('-'*(8*len(list1)-4))    
    
k=eval(input("按1进入温度排序；按2进入图标展现\n 请选择："))
if k==1:
    paixu()
elif k==2:
    tu()
