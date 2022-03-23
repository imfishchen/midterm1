kilometer=float(input("請輸入路程公里數(km):"))
if kilometer<=1.5:
    print("所需車資為:75")
elif kilometer>1.5 and kilometer*1000%250==0:
    m=(kilometer-1.5)*1000
    total=75+(m//250)*5
    print(total)
elif kilometer>1.5 and kilometer*1000%250!=0:
    n=(kilometer-1.5)*1000
    total=75+(n//250+1)*5
    print(total)