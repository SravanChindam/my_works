class sum:
    def inputs(self):
        self.a=int(input("enter a value: "))
        self.b=int(input("enter b value: "))
    def logic(self):
        self.total=self.a+self.b
    def output(self):
        print("total sum = ",self.total)
s=sum()
s.inputs()
s.logic()
s.output()