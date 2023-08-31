#INSTANCE METHOD
class student:
    course="bsc-mpcs"   #class level data members
    location="lxpt"     #class level data members
    def get_student_data(self):                         #instance method
        self.sno=int(input("enter student number:"))    #instance level datamembers
        self.sname=input("enter student name: ")
        self.smarks=float(input("enter student marks:"))
        self.group=student.course     #accessing class level datamembers into instance method
        self.address=student.location #  ''''''''''''''''''''''''''''''''''''''''''
    def display_student_data(self):
        print("student number: {}".format(self.sno))
        print("student name: {}".format(self.sname))
        print("student marks: {}".format(self.smarks))
        print("Group name: {}".format(self.group))
        print("college address: {}".format(self.address))
s1=student()   #Object 1 of student class
s2=student()   #Object 2 of student class
s1.get_student_data()   #Instance method calling with respect to object 1
print('-'*30)
print("Student-1 Details")
s1.display_student_data()
s2.get_student_data()       #Instance method calling with respect to object 2
print('-'*30)
print("Student-2 Details")
s2.display_student_data()