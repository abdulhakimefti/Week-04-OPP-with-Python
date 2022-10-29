class School:
    def __init__(self,SchoolName):
        self.schoolName = SchoolName
        print('school init')

class Grade:
    def __init__(self,gradeName):
        self.gradeName = gradeName
        print('Grade Class init call')

class Student(School,Grade):
    def __init__(self,name,gradeName,school):
        self.name = name
        # super().__init__(gradeName)
        # super().__init__(school)
        Grade.__init__(self,gradeName)
        School.__init__(self,school)
        print("Dooonee")


anata_j = Student('AJ','MBA','UK School')
print(anata_j.name,anata_j.gradeName,anata_j.schoolName)