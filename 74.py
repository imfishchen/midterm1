list1=["red","blue","red","green"]
count1=0
for i in range(10):
    answer=0
    color=str(input("")).split(" ")
    for i in range(4):
        if color[i]==list1[i]:
            print("1",end="")
            answer=answer+1
        elif color[i] in list1:
            print("2",end="")
        else:
            print("3")
    if answer==4:
        print("答案正確")
        break
    count1=count1+1
    if count1==10:
        print("挑戰失敗")
