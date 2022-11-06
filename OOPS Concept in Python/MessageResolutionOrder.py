class A:
    def __init__(self):
        print("This is A")
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")
class B:
    def __init__(self):
        print("This is B")
    def f1(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("This is C")
    def f(self):
        super().f1()
        
c1=C()
c1.f()

