class Parent():
    def func1(self):
        print("this is Parent class")
class Child1(Parent):
    def func2(self):
        print("this is Child1 class")
class Child2(Parent):
    def func3(self):
        print("this is Child2 class")        
obj=Child1()

obj.func1()
obj.func2()   
#obj.func3() 