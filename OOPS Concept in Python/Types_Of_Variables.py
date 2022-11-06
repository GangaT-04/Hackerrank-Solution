class car:
    wheels=4 #class namespace or variables
    def __init__(self):
        self.col='black'      #instance namespace or variables
        self.brand='Audi'
c1=car()
c2=car()
car.wheels=5
print(c1.col,c1.brand,c1.wheels)
print(c2.col,c2.brand,c2.wheels)
