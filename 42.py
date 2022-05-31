a=int(input(""))
b=int(input(""))
c=int(input(""))
k=b**2-4*a*c
if k>0:
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print(x1,x2,end=" ")
elif k==0:
    x1=-b/2*a
    print(x1)
elif k<0:
    print("無解")