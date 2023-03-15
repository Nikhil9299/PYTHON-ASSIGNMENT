#2parent 1child

class Father():
    def func1(self):
        print("this is Father class")
class Mother():
    def func2(self):
        print("this is Mother class")
class Child(Father,Mother):
    def func3(self):
        print("this is Child class")        
obj=Child()
obj.func1()
obj.func2()   
obj.func3() 