str1=str(input("檢測的字串(end):"))
test=str(input("檢測的單一字元:"))
if str1=="end":
    print("測驗結束")
else:
    count1=str1.count(test)
    print("字元",test,"出現的次數為:",count1)