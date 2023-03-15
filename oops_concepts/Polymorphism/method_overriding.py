#diff class 
#same func or method name
#diff parameters


class A:
    def display(self):
        print("this is class A")
class B(A):
    def display(self):
        super().display()
        print("this is class B")
    



obj=B()
obj.display()   