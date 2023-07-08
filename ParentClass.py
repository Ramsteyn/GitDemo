class Calculator:
    num = 100
    c = 100

    def __init__(self, a, b):
        self.i = a
        self.j = b

    def add(self):
        return self.i + self.j

    def add1(self):
        d = Calculator.num + Calculator.c
        print(d)




obj = Calculator(4, 5)
print(obj.add())
obj.add1()
