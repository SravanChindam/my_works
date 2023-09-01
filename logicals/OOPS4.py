#class level method
class employee:
    @classmethod
    def employee_data(cls):
        employee.company_name="TCS"
        employee.location="HYD"
        cls.employee_state()

    @classmethod
    def employee_state(cls):
        employee.state1 = "TELANGANA"


    def employee_details(self):
        self.emp_num=int(input("enter emp number:"))
        self.emp_name=input("enter emp name: ")
    def output_employee_details(self):
        print("employee number",self.emp_num)
        print("employee name",self.emp_name)
        print("company name:",employee.company_name)
        print("location:",employee.location)
        print("employee state:",employee.state1)
e1=employee()
e1.employee_data()
e1.employee_details()
e1.output_employee_details()
e2=employee()
e2.employee_data()
e2.employee_details()
e2.output_employee_details()

