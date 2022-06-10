day=input("請輸入月及日:").split(" ")
print(day[1])
if day[0]==1:
    if day[1]<21:
        print("星座為:Capricorn")
    else:
        print("星座為:Aquarius")

elif day[0]==2:
    if day[1]<19:
        print("星座為:Aquarius")
    else:
        print("星座為:Pisces")

elif day[0]==3:
    if day[1]<21:
        print("星座為:Pisces")
    else:
        print("星座為:Aries")

elif day[0]==4:
    if day[1]<21:
        print("星座為:Aries")
    else:
        print("星座為:Taurus")

elif day[0]==5:
    if day[1]<22:
        print("星座為:Taurus")
    else:
        print("星座為:Gemini")

elif day[0]==6:
    if day[1]<22:
        print("星座為:Gemini")
    else:
        print("星座為:Cancer")

elif day[0]==7:
    if day[1]<23:
        print("星座為:Leo")
    else:
        print("星座為:Virgo")

elif day[0]==8:
    if day[1]<24:
        print("星座為:Virgo")
    else:
        print("星座為:Libra")

elif day[0]==9:
    if day[1]<24:
        print("星座為:Libra")
    else:
        print("星座為:")

elif day[0]==10:
    if day[1]<24:
        print("星座為:Libra")
    else:
        print("星座為:Scorpio")

elif day[0]==11:
    if day[1]<23:
        print("星座為:Scorpio")
    else:
        print("星座為:Sagittarius")

elif day[0]==12:
    if day[1]<22:
        print("星座為:Sagittarius")
    else:
        print("星座為:Capricorn")


