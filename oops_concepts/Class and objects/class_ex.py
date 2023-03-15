class Student:
    d=5
    print("this is class")
    def display(self):
        a=10
        b=20
        print(a,b)
obj=Student()
obj.display()
print(obj.d)        
obj.d=30
print(obj.d)   

