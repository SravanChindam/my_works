num=int(input("enter a number: "))
x=len(str(num))
total=0
y=num
while y>0:
    digit=y%10
    total=(digit**x)+total
    y=y//10
print(total)
if num==total:
    print("Given num is an armstrong number")
else:
    print("not an armstrong number")