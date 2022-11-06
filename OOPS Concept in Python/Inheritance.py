class A:
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")
class B:
    def f3(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")
class C(A,B):
    def f5(self):
        print("f5 is working")
        '''
#Single Level Inheritance
b1=B()
b1.f1()
b1.f2()
b1.f3()
b1.f4()'''

#Mutilevel Inheritance
c1=C()
c1.f1()
c1.f2()
c1.f3()
c1.f4()
c1.f5()


    
    
