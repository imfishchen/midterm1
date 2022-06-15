
list1=list(map(int,input("輸入值為:").split(",")))
print(type(list1[0]))
# print(list1)
list1.sort()
min=list1
#print(min)
list2=list1.copy()
list2.reverse()
max=list2
#print(max)
b=int(min[0]*10000+min[1]*1000+min[2]*100+min[3]*10+min[4])
print(b)
c=int(max[0]*10000+max[1]*1000+max[2]*100+max[3]*10+max[4])
print(c)
d=c-b
print("最大數值列瑀最小數值列差值為:",d)