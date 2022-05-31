word=input("輸入摩斯密碼:").split(" ")
if word=="-----" or word=="Dah-Dah-Dah-Dah-Dah":
    print(1)
elif word==".----" or word=="Dit-Dah-Dah-Dah-Dah":
    print(2)
elif word=="..---" or word=="Dit-Dit-Dah-Dah-Dah":
    print(3)
elif word=="...--" or word=="Dit-Dit-Dit-Dah-Dah":
    print(4)
elif word=="....-" or word=="Dit-Dit-Dit-Dit-Dah":
    print(5)
elif word=="....." or word=="Dit-Dit-Dit-Dit-Dit":
    print(6)
elif word=="-...." or word=="Dah-Dit-Dit-Dit-Dit":
    print(7)
elif word=="--..." or word=="Dah-Dah-Dit-Dit-Dit":
    print(8)
elif word=="---.." or word=="Dah-Dah-Dah-Dit-Dit":
    print(9)
elif word=="----." or word=="Dah-Dah-Dah-Dah-Dit":
    print(10)