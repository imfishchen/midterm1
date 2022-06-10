from numpy import rad2deg


dict1={"123":"456","456":"789","789":"888","336":"558","775":"666","566":"221",}
dict2={"123":9000,"456":5000,"789":6000,"336":10000,"775":12000,"566":7000,}
n=int(input("輸入查詢組數N為:"))
for i in range(n):
    kw=input(" ").split(" ")
    if dict1[kw[0]]==kw[1]:
        print(dict2[kw[0]])
    else:
        print("error")