question=str(input("輸入:"))
answer="1234"

acount=0
bcount=0
for i in question:
    for j in answer:
        if i==j:
            if question.index(i)==answer.index(j):
                acount=acount+1
            else:
                bcount=bcount+1

print(str(acount)+"A"+str(bcount)+"B")