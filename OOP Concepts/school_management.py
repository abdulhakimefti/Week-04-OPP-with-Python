class School :
    def __init__(self,name,address,pricipal=''):
        self.name = name
        self.address = address
        self.principal = pricipal
        self.grades=[]
    def addGrade(self,name,teacher):
        newGrade = Grade(name,teacher)
        self.grades.append(newGrade)
   

class Grade :
    def __init__(self,teacehr,name):
        self.students=[]
        self.teacher = teacehr
        self.name = name
    def __repr__(self) -> str:
        return f'{self.name} with {self.teacher}'
    def __del__(self):
        return f'deleing {self.name}'

oxford= School('Oxford','mirpur','jhankar mahbub')
oxford.addGrade('rahat','c++')
print(oxford.grades)