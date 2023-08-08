n = int(input("enter a number : "))  #30
lst = list()
for num in range(2,n+1): #(2,30+1)--->(2,30)
    res = "PRIME"
    for i in range(1,num):
        if(num%2==0):
            res = "NOT PRIME"
            break
    if(res=="PRIME"):
        lst.append(num)
else:
    print("list of prime numbers")
    for v in lst:
        print(v)