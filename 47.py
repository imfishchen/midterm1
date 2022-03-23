allmedal={}
n=int(input("輸入筆數n:"))
for i in range(n-1):
    medal=input("獎牌:")
    medalnum=input("數量:")
    allmedal[medal]=medalnum

for i in allmedal:
    print(i,"牌得到",allmedal[i],"面")