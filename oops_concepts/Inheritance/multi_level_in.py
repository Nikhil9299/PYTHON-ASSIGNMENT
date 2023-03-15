#parent --> child --> grandchild

class Parent():
    def func1(self):
        print("this is parent class")
class Child(Parent):
    def func2(self):
        print("this is child class")
class GrandChild(Child):
    def func3(self):
        print("this is GrandChild class")        
obj=GrandChild()
obj.func1()
obj.func2()   
obj.func3() 