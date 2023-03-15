class Parent():
    def func1(self):
        print("this is parent class")
class Child(Parent):
    def func2(self):
        print("this is child class")
obj=Child()
obj.func2()
obj.func1()                