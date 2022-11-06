class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self,b,c,r):
            self.brand=b
            self.cpu=c
            self.ram=r
        def show(self):
            print(self.brand,self.cpu,self.ram)
        


s1=Student('Ganga',1)
s2=Student('Yamuna',2)

s1.show()
lap=Student.Laptop("asus","i3",4)
lap.show()
s2.show()
lap1=Student.Laptop("hp","i3",4)
lap1.show()
