allmedal={}
n=int(input("獎牌筆數:"))
for i in range(n):
    medal=input("獎牌:")
    medalnum=input("數量:")
    allmedal[medal]=medalnum
    listkey1=list(allmedal.keys())
    listvalue1=list(allmedal.values())
for i in range(len(listkey1)):
    print("%s牌得到%d面" % (listkey1[i],listvalue1[i]))