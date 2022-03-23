list1=[["學號","姓名","系別"],["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
a=str(input("輸入查詢學號為:"))
if a=="123":
    print("學生資料為:",(" ").join(list1[1]))
elif a=="456":
    print("學生資料為:",(" ").join(list1[2]))
elif a=="789":
    print("學生資料為:",(" ").join(list1[3]))
elif a=="321":
    print("學生資料為:",(" ").join(list1[4]))
elif a=="654":
    print("學生資料為:",(" ").join(list1[5]))
