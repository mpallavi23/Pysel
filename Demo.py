class Calc:
    n = 10   #class variable

    def __init__(self, a, b):
        #a, b are instance variables
        self.a = a
        self.b = b
        print("Default constructor - It runs without being called")

    def getdata(self):
        print("Inside class method")

    def addTest(self):
        return self.a+self.b+self.n  #also can be called as Calc.n as n is a class variable



o = Calc(2, 3)
o.getdata()
print(o.n)
print(o.addTest())