list1=[]
ans=0
for i in range(5):
    list1.append(input("輸入:"))
    if list1[i]=="a" or list1[i]=="A":
        ans=ans+1
    elif list1[i]=="2":
        ans=ans+2
    elif list1[i]=="3":
        ans=ans+3
    elif list1[i]=="4":
        ans=ans+4
    elif list1[i]=="5":
        ans=ans+5
    elif list1[i]=="6":
        ans=ans+6
    elif list1[i]=="7":
        ans=ans+7
    elif list1[i]=="8":
        ans=ans+8
    elif list1[i]=="9":
        ans=ans+9
    elif list1[i]=="10":
        ans=ans+10
    elif list1[i]=="j" or list1[i]=="J":
        ans=ans+11
    elif list1[i]=="q" or list1[i]=="Q":
        ans=ans+12
    elif list1[i]=="k" or list1[i]=="K":
        ans=ans+13
print(ans)
