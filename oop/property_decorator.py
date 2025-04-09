class Student:
    def __init__(self, name, studentnum):
        self._name = name
        self._studentnum = studentnum

    @property
    def name(self):
        return self._name
    
    @property
    def studentnum(self):
        return self._studentnum
    
    @name.setter
    def name(self, name):
        if len(name) < 2:
            raise ValueError("Name must be at least two characters or more")
        self._name = name

    @studentnum.setter
    def studentnum(self, studentnum):
        if not isinstance(studentnum, int):
            raise ValueError("Student num must be an interger")
        self._studentnum = studentnum

s1 = Student("Dylan", 123)

print(s1.name)
print(s1.studentnum)

s1.name = 'A'
