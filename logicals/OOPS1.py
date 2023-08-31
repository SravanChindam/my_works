class student:
    classroom="BSC-Mpcs"  #class level data members
    clg_name="GDC-LXPT"     #class level data members


s1=student()   #object1 for student class
s2=student()   #object2 for student class
print("content of s1 before adding:",s1.__dict__)
print("content of s2 before adding:",s2.__dict__)
s1.sno=int(input("enter s1 student number: "))        #Adding Instance Data memebrs through an object to s1
s1.sname= input("enter s1 student name: ")
s1.marks= float(input("enter s1 student marks: "))
s1.classs=s1.classroom
s1.college=student.clg_name
s2.sno=int(input("enter s2 student number: "))       #Adding Instance Data memebrs through an object to s2
s2.sname=input("enter s2 student name: ")
s2.marks= float(input("enter s2 student marks: "))
s2.classs=s1.classroom
s2.college=student.clg_name
print("content of s1 after adding: ",s1.__dict__)
print("content of s2 after adding:",s2.__dict__)
print("*"*50)
print("student1 details")
print("*"*50)

for a,b in s1.__dict__.items():
    print("{}-->{}".format(a,b))
print("*" * 50)

print("student2 details")
print("*"*50)

for c,d in s2.__dict__.items():
    print("{}-->{}".format(c,d) )
