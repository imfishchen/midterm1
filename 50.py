alll=set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
englishpass=set(["John","Mary","Fiona","Claire","Ben","Bill"])
mathpass=set(["Mary","Fiona","Claire","Eva","Ben"])

print("英文與數學都及格",englishpass & mathpass)
print("數學不及格",alll - mathpass)
print("英文及格且數學不及格",englishpass & (alll-mathpass))