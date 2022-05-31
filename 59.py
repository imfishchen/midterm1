money=int(input("輸入金額:"))
hundred=money//100
fifty=(money-hundred*100)//50
ten=(money-hundred*100-fifty*50)//10
five=(money-hundred*100-fifty*50-ten*10)//5
one=money-hundred*100-fifty*50-ten*10-five*5
total=hundred+fifty+ten+five+one
print(total)