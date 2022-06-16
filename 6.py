
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
print(len(list1))
if 1<=len(list1)<=7:
    if len(list1)==1:
        b=int(min[0])
        print(b)
        c=int(max[0])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
    if len(list1)==2:
        b=int(min[0]*10+min[1])
        print(b)
        c=int(max[0]*10+max[1])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
    elif len(list1)==3:
        b=int(min[0]*100+min[1]*10+min[2])
        print(b)
        c=int(max[0]*100+max[1]*10+max[2])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
    elif len(list1)==4:
        b=int(min[0]*1000+min[1]*100+min[2]*10+min[3])
        print(b)
        c=int(max[0]*1000+max[1]*100+max[2]*10+max[3])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
    elif len(list1)==5:
        b=int(min[0]*10000+min[1]*1000+min[2]*100+min[3]*10+min[4])
        print(b)
        c=int(max[0]*10000+max[1]*1000+max[2]*100+max[3]*10+max[4])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
    elif len(list1)==6:
        b=int(min[0]*100000+min[1]*10000+min[2]*1000+min[3]*100+min[4]*10+min[5])
        print(b)
        c=int(max[0]*100000+max[1]*10000+max[2]*1000+max[3]*100+max[4]*10+min[5])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
    elif len(list1)==7:
        b=int(min[0]*1000000+min[1]*100000+min[2]*10000+min[3]*1000+min[4]*100+min[5]*10+min[6])
        print(b)
        c=int(max[0]*1000000+max[1]*100000+max[2]*10000+max[3]*1000+max[4]*100+min[5]*10+min[6])
        print(c)
        d=c-b
        print("最大數值列瑀最小數值列差值為:",d)
else:
    print("錯誤")