class Mobile():
    def __init__(self,brand,battery,ram,camera,price):
        self.brand=brand
        self.battery=battery
        self.ram=ram
        self.camera=camera
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Battery:",self.battery)
        print("ram:",self.ram)
        print("Brand:",self.camera)
        print("Brand:",self.price)
        print("------------------------")


obj=Mobile("apple","4000mah","6gb","48mp","85000")
obj.display()
obj_2=Mobile("oneplus","5000mah","8gb","48mp","48000")
obj_2.display()


