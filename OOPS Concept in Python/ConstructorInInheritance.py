class A:
    def __init__(self):
        print("This is A")
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")
class B(A):
    def __init__(self):
        print("This is B")
        super().__init__()
    def f3(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")
a1=B()
