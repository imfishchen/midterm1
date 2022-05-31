n=int(input("輸入比數n:"))
dict1={}
for i in range(n):
    a=input(" ").split(" ")
    dict1[a[0]]=a[1]
what=input("輸入欲查詢單字:")
if what in dict1:
    b=dict1.setdefault(what)
    print(str(what)+str("中文意思為")+str(b))