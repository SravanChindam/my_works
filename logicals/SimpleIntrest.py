#calculating simple intrest and total amount to pay
Principle_Amount = float(input("enter a amount : "))
time_period = int(input("enter a time in terms of months : "))
RateOfIntrest = int(input("enter percentage : "))
#formula for simple intrest
#taking simple intrest as si
si = (Principle_Amount*time_period*RateOfIntrest) / 100
#formula for totalamount
#taking total amount as ta
ta = Principle_Amount + si
print("simple intrest is : ",si)
print("total amount is : ",ta)
