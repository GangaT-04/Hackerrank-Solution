#instance Methods
class Student:
    clg="Anna University"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        return (self.m1+self.m2+self.m3)/3.0
    #accessor Method
    def get_m1(self):
        return self.m1
    #Mutator Method
    def set_m1(self,value):
        self.m1=value

    #class Method
    @classmethod
    def info(cls):
        return cls.clg
    @staticmethod
    def info1():
        print("This is Student Class...")
s1=Student(100,100,100)
s2=Student(90,90,90)

print(s2.set_m1(80))
print(s2.average())
print(s2.get_m1())
Student.info1()
print(Student.info())

