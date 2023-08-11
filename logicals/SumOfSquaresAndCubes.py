num = int(input("enter how many numbers sum u want to find : "))
print("\tNatNums\t\tSqures\t\tcubes")
natnums = 0
sqrs = 0
cubes = 0
i = 1
while(i<=num):
    print("\t\t{}\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
    sqrs = sqrs + i**2
    cubes = cubes + i**3
    i = i + 1