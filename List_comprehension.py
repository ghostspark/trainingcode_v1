list2=[10,21.2,15,16,-9]
for i in range(5):
    print("星期"+str(i+1)+":"+str(list2[i])+"摄氏度")
sum1=sum([10,21.2,15,16,-9])
ave=(sum1)/5
print("平均温度是"+str(ave)+"摄氏度")
#原创：列表推导式
print(sum((list2[i] for i in range (len(list2))))/5)
