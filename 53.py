n=int(input("輸入n值:"))
dict1={}
for i in range(n):
    a=input("請輸入姓名:")
    b=input("請輸入電子郵件:")
    dict1[a]=b
what=input("輸入欲查詢單字:")
if what in dict1:
    c=dict1.setdefault(what)
    print(str(what)+str("電子郵件帳號為")+str(c))