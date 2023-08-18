while(True):             #if you want to try again and again
    #Using Function for checking leap year or not
    def check_year(year):
        return((year%4==0) and (year%100!=0)or(year%400==0))
    year = int(input("enter a year: "))
    a=check_year(year)
    if (a):
        print("Leap year")
    else:
        print("not a Leap year")

    year = int(input("enter a year: "))

    #Using if condition for checking leap year or not

    if (year%4==0) and (year%100!=0) or (year%400==0):
        print("{} is Leap year".format(year))
    else:
        print("{} is not a Leap year".format(year))