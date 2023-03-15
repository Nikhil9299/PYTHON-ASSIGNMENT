#same class 
#same func or method name
#diff parameters
#to overcome method overloading we use default parameters

class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=30):
        return a+b+c
obj=A()
print(obj.sum(10,20,2))    