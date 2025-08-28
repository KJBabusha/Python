# Create a class representing anything you like
class Smartphone:
    def __init__(self, year, brand, model):
        self.series =year # Attribute
        self.make=brand #Attribute
        self.model= model #Attribute 
        self.__battery = 100 # Encapsulation attribute(private)
    def buy(self): #method
         print(f"{self.series},{self.make}, {self.model} it's the latest!")
    
    def use(self,hours):
        self.__battery -= hours * 10
        if self.__battery < 0:
            self.__battery = 0
        print(f"used for {hours} hours. Battery at {self.__battery}%")

    def get_battery(self):
        return self.__battery
    


#create Inheritance: Tesla is a kind of Smartphone
class Automobile(Smartphone):
    def buy(self):
        print(f"{self.series}, {self.make}, {self.model} it's a smart Automobile")
    
    def milage_power(self, power):
        print(f"Milage {power} power used today.")
        
#create objects
new_phone= Smartphone(2025, "Vivo", "Y21")
new_phone.buy()
new_phone.use(4)
print("Battery left", new_phone.get_battery(), "%" )

car= Automobile(2020, "Tesla", "XB001")
car.buy()
car.use(6)
car.milage_power(300)
print("Battery Left", car.get_battery(), "%")