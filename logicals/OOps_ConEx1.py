#  Constructor: constructor is one of the special method in python which is automatically-implicitly called by PVM during object creation and whose purpose is to initialize the objects.
#  constuctors are two types: 1) Default constructors 2) Parameterized constructors
class student:
    def __init__(self):  #default constructor
        self.sno=31
        self.sname="sravan"
s=student()  #object1
print("data of s",s.__dict__)
t=student()   #object2
print("data of t",t.__dict__)

