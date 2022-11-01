class Student:
    def __init__(self,name,id,marks):
        self.name= name
        self._id = id
        self.marks = marks
    @property
    def studentId (self):
        return self._id


chowdhury = Student('cc',234,42345)
print(chowdhury._id)
chowdhury._id= 77
print(chowdhury._id)