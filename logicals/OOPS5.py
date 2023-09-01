#static method
class student:
    def student_data(self):
        self.student_num= 12345
        self.student_name="sravan"
        self.student_class="BSC"
class teacher:
    def teacher_data(self):
        self.teacher_num=3232
        self.teacher_name="sushmitha"
        self.teacher_address="Choutapalli"
class parents:
    def parents_data(self):
        self.fathera_name=input("enter father name: ")
        self.mother_name=input("enter mother name: ")
class display:
    @staticmethod
    def display_alldata(obj):
        for a,b in obj.__dict__.items():
            print("{}--->{}".format(a,b))
s=student()
t=teacher()
p=parents()
s.student_data()
t.teacher_data()
p.parents_data()
display.display_alldata(s)
display.display_alldata(t)
display.display_alldata(p)