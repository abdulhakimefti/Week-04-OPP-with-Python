class Employee:
    def __init__(self,name,id,salary,position,exp):
        self.name = name
        self.id = id 
        self.salary  = salary
        self.position = position

class Developer(Employee):
    def __init__(self,name,id,salary,position,exp,tech,focus):
        self.tech = tech
        self.focus = focus
        super().__init__(name,id,salary,position,exp)

class Testion(Employee):
    pass

class Sales(Employee):
    pass