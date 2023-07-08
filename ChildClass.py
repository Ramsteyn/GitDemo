from ParentClass import Calculator


class ChildClass(Calculator):
    num2 = 200


    def __init__(self, a, b):
        self.i = a
        self.j = b
        # Initiating parent class constructor
        Calculator.__init__(self, a, b)

    def GetCompleteData(self):
        return self.num2 + self.num + self.add()




obj = ChildClass(2, 3)

print(obj.GetCompleteData())
