num = int(input("enter how many mul tables you want: "))
lst = list()
for i in range(1,num+1):
    val = int(input("enter {} number : ".format(i)))
    lst.append(val)
else:
    print("List of numbers for mul tables: {} ".format(lst))
    for x in lst:
        print("mul table for",x)
        for y in range(1,11):
            print("{} x {} = {}".format(x,y,x*y))