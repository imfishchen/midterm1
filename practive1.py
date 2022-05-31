english=str(input("請輸入一串小寫英文:"))
r1="a"
r2="e"
r3="i"
r4="o"
r5="u"
if r1 in english or r2 in english or r3 in english or r4 in english or r5 in english:
    rr1=english.replace("a", ".")
    rr2=rr1.replace("e", ".")
    rr3=rr2.replace("i", ".")
    rr4=rr3.replace("o", ".")
    rr5=rr4.replace("u", ".")
    print(rr5)