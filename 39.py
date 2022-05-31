n=int(input("請輸入菱形行數："))
m=n
d=n
for i in range(1,n+1):
    print(" "*(m-1),"*"*(2*i-1))
    m-=1
    if i==n:
        for y in range(1,n):
            print(" "*y,"*"*(2*d-3))
            d-=1




# n=int(input(""))
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end='')
#     for j in range(i+1):
#         print("*",end='')
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

# n=int(input(""))
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end='')
#     for j in range(2*i+1):
#         print("*",end='')
#     print()

#     n=int(input(""))
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print("*",end='')
#     print()