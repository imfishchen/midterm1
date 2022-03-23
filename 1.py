list1=[19,22,33]
list2=["19","22","33"]
print(list1)
print(list2)
print((" ,").join(str(i) for i in list1))#以逗号为间隔
print((" ").join(list2))