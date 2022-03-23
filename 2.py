electricity=int(input("輸入:"))
if electricity<=120:
    summer=electricity*2.10
    nosummer=electricity*2.10
    print("Summer months:",summer)
    print("Non-Summer months:",nosummer)
elif 120<electricity<=330:
    summer=120*2.10+(electricity-120)*3.02
    nosummer=120*2.10+(electricity-120)*2.68
    print("Summer months:",summer)
    print("Non-Summer months:",nosummer)
elif 330<electricity<=500:
    summer=120*2.10+210*3.02+(electricity-330)*4.39
    nosummer=120*2.10+210*2.68+(electricity-330)*3.61
    print("Summer months:",summer)
    print("Non-Summer months:",nosummer)
elif 500<electricity<=700:
    summer=120*2.10+210*3.02+170*4.39+(electricity-500)*4.97
    nosummer=120*2.10+210*2.68+170*3.61+(electricity-500)*4.01
    print("Summer months:",summer)
    print("Non-Summer months:",nosummer)
elif 700<electricity:
    summer=120*2.10+210*3.02+170*4.39+200*4.97+(electricity-700)*5.63
    nosummer=120*2.10+210*2.68+170*3.61+200*4.01+(electricity-700)*4.50
    print("Summer months:",summer)
    print("Non-Summer months:",nosummer)