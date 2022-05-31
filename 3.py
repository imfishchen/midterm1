animals = "鼠牛虎免龍蛇馬羊猴雞狗豬"
year = int(input(""))
a = (animals[(year-2008) % 12])
if a =="鼠":
    print("rat")
elif a =="牛":
    print("ox")
elif a =="虎":
    print("tiger")
elif a =="兔":
    print("rabbit")
elif a =="龍":
    print("dragon")
elif a =="蛇":
    print("shake")
elif a =="馬":
    print("horse")
elif a =="羊":
    print("sheep")
elif a =="猴":
    print("monkey")
elif a =="雞":
    print("rooster")
elif a =="狗":
    print("dog")
elif a =="豬":
    print("pig") 