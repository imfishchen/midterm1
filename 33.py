grade=[]
sum=0
chinese=int(input("國文:"))
english=int(input("英文:"))
wjf=int(input("微積分"))
pe=int(input("體育"))
cssj=int(input("程式設計"))
sum=chinese+english+wjf+pe+cssj
avg=sum/5
print("平均分數:",avg)
print("最高分科目",max(chinese,english,wjf,pe,cssj))
print("最低分科目",min(chinese,english,wjf,pe,cssj))


