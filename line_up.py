import urllib.request as r
b=input("请输入城市（拼音）：")
url='http://api.openweathermap.org/data/2.5/forecast?q='+b+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'    

data=r.urlopen(url).read().decode('utf-8')
import json
import numpy as np
import matplotlib.pyplot as plt
data=json.loads(data)
for i in range(5):
    print("第{}天:".format(i+1))
    print("  当天的温度是----------"+str(data['list'][i]['main']['temp']))
    print("  当天的最低温度是------"+str(data['list'][i]['main']['temp_min']))
    print("  当天的最高温度是------"+str(data['list'][i]['main']['temp_max']))
    print("  当天气压为------------"+str(data['list'][i]['main']['pressure']))
    print("  当天体感温度----------"+str(data['list'][i]['main']['feels_like']))
    print("·时间："+str(data['list'][i]['dt_txt']))
    print("=================================================================")
list1=[data['list'][0]['main']['temp'],data['list'][1]['main']['temp'],data['list'][2]['main']['temp'],data['list'][3]['main']['temp'],data['list'][4]['main']['temp']]
list2=sorted(list1)
j=input("......输入任意键继续......")
print("==============温度排序=============")
print(list2)
print("未来5天中最高日气温是"+str(list2[0])+";")
print("未来5天中最低日气温是"+str(list2[4])+".")
j=input("....输入任意键继续—进入图表......")
x = np.array(['第1天','第2天','第3天','第4天','第5天'])
y = np.array([data['list'][0]['main']['temp'],data['list'][1]['main']['temp'],data['list'][2]['main']['temp'],data['list'][3]['main']['temp'],data['list'][4]['main']['temp']])
plt.plot(x,y,'r',lw=2)
plt.show()
