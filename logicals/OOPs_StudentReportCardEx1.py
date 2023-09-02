#student report card of 6 subjects
class student_report_card:
    def __init__(self):
        while(True):
            self.student_number=int(input("enter student number: "))
            if self.student_number>=0:
                break
            print("{} is invalid student number".format(self.student_number))
        self.student_name=input("enter student name: ")
        #accessing sub1 marks
        while(True):
            self.telugu_marks=float(input("enter telugu marks: "))
            if self.telugu_marks>0 and self.telugu_marks<100:
                break
            print("{} is invalid marks in telugu ",self.telugu_marks)
        while(True):
            self.english_marks=float(input("enter english marks: "))
            if self.english_marks>0 and self.english_marks<100:
                break
            print("{} is invalid marks in english",self.english_marks)
        while(True):
            self.maths_marks=float(input("enter maths marks: "))
            if self.maths_marks>0 and self.maths_marks<100:
                break
            print("{} is invalid marks in maths".format(self.maths_marks))
        while(True):
            self.Compscience_marks=float(input("enter Compscience marks: "))
            if self.Compscience_marks>0 and self.Compscience_marks<100:
                break
            print("{} is invalid marks in science".format(self.Compscience_marks))
        while(True):
            self.physics_marks=float(input("enter Physics marks: "))
            if self.physics_marks>0 and self.physics_marks<100:
                break
            print("{} is invalid marks in social".format(self.physics_marks))
    def calculations(self):
        self.total_marks=self.telugu_marks+self.english_marks+self.maths_marks+self.Compscience_marks+self.physics_marks
        self.percentage=(self.total_marks/500)*100
        if (self.telugu_marks<40) or  (self.english_marks<40) or (self.maths_marks<40) or (self.Compscience_marks<40) or (self.physics_marks<40):
            self.Grade="FAIL"
        else:
            if(self.total_marks>=450) and (self.total_marks<=500):
                self.Grade="O"
            elif (self.total_marks>=400) and (self.total_marks<=449):
                self.Grade="A"
            elif (self.total_marks>=350) and (self.total_marks<=399):
                self.Grade="B"
            elif (self.total_marks>=300) and (self.total_marks<=349):
                self.Grade="C"
            elif (self.total_marks>=250) and (self.total_marks<=299):
                self.Grade="D"
            elif (self.total_marks>=200) and (self.total_marks<=249):
                self.Grade="E"
    def marks_report_output(self):
        print("=" * 50)
        print("\t\tStudent Marks Report:")
        print("=" * 50)
        print("\tStudent Number:{}".format(self.student_number))
        print("\tStudent Name:{}".format(self.student_name))
        print("\tStudent Marks in Telugu:{}".format(self.telugu_marks))
        print("\tStudent Marks in English:{}".format(self.english_marks))
        print("\tStudent Marks in Maths:{}".format(self.maths_marks))
        print("\tStudent Marks in ComputerScience:{}".format(self.Compscience_marks))
        print("\tStudent Marks in Physics:{}".format(self.physics_marks))
        print("-" * 50)
        print("\tStudent Total Marks:{}".format(self.total_marks))
        print("\tStudent Percentage of Marks: {}".format(self.percentage))
        print("\tStudent Grade:{}".format(self.Grade))
        print("=" * 50)
re=student_report_card()
re.calculations()
re.marks_report_output()












