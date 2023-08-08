num = int(input("enter a number for mul tables: "))
for i in range(1,num+1):
    print("Mul table for ",i)
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))