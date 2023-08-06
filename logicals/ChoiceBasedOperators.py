print("ARITHMETIC OPERATORS")
print("1.Addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.floor division")
print("6.modulo division")
print("7.exponentation")
print("8.exit")
while(True):
    your_choice = int(input("enter your choice : "))
    match (your_choice):
        case 1:
            a = int(input("enter a first number: "))
            b = int(input("enter a second number: "))
            print("sum({},{}) = {}".format(a, b, a + b))
        case 2:
            a = int(input("enter a first number: "))
            b = int(input("enter a second number: "))
            print("substraction({},{}) = {}".format(a, b, a - b))
        case 3:
            a = int(input("enter a first number: "))
            b = int(input("enter a second number: "))
            print("multiplication({},{}) = {}".format(a, b, a * b))
        case 4:
            a = int(input("enter a first number: "))
            b = int(input("enter a second number: "))
            print("division({},{}) = {}".format(a, b, a / b))
        case 5:
            a = int(input("enter a first number: "))
            b = int(input("enter a second number: "))
            print("floordivision({},{}) = {}".format(a, b, a // b))
        case 6:
            a = int(input("enter a first number: "))
            b = int(input("enter a second number: "))
            print("modulodivision({},{}) = {}".format(a, b, a % b))
        case 7:
            a = int(input("enter a number for base: "))
            b = int(input("enter a number for power: "))
            print("modulodivision({},{}) = {}".format(a, b, a ** b))
        case 8:
            print("exit from the program")
        case _:
            print("sorry try again,your choice selection is wrong!!!")
    print("-----------------")






