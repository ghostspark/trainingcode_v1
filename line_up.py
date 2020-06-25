import numpy as np
import matplotlib.pyplot as plt
import re

Dcountry={"星期一":"18度，雨天","星期二":"15度，晴天","星期三":"10度，晴天","星期四":"8度，雨天","星期五":"12度，晴天","星期六":"13度，多云","星期日":"12度，雾"}
L1=list(Dcountry.keys())
L2=list(Dcountry.values())
for i in range(7):
    print(str(L1[i])+str(L2[i]))
print("星期三，"+str(Dcountry.get("星期三",0)))
print("最高温度是："+str(Dcountry.get("星期一",0)))

#折线图
x = np.array(["星期一","星期二","星期三","星期四","星期五","星期六","星期日"])
y = np.array([18,15,10,8,12,13,12])
plt.plot(x,y,'r',lw=2)
plt.show()
