M=int(input("小明身上有幾元:"))
N=int(input("販賣機有幾種飲料"))
MM=0
for i in range(1,N+1):
    P=int(input(""))
    if P<=M:
        MM=MM+1
print(MM)