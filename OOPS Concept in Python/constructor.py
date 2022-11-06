class Computer:
    def __init__(self):
        self.name="Ganga"
        self.age=22
    def update(self):
        self.age=23
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
if c2.compare(c1):
    print("They are same age")
else:
    print("Not")
          
print(c1.name)
print(c2.name,c2.age)
'''print(id(c1))
print(id(c2))'''
