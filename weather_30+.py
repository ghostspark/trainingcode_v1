import requests as r
from xpinyin import Pinyin
import re
import os
weather={}
list1=['保定','北京','天津','石家庄','大同','乌鲁木齐',
       '齐齐哈尔','哈尔滨','太原','青岛','辽宁','大连',
       '重庆','武汉','长沙','成都','江门','杭州','广州','茂名'
       ,'襄阳','深圳','珠海','西安','潮州','中山','梅州','东沙',
       '江门','汕头','亳州']
headers={
    'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    
}
for i in range(len(list1)):
    list1_pinyin=Pinyin().get_pinyin(list1[i],'')
    url='http://api.openweathermap.org/data/2.5/forecast?q='+list1_pinyin+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'    
    response=r.get(url,headers=headers)
    html=response.text
    print(html)
    description=re.findall('{"id":.*?,"main":".*?","description":"(.*?)","icon":"*?"}',html)
    weather[list1[i]]=str(description)
with open('city1.txt','w') as f2:
    f2.write(str(weather))
print('保存完成')
