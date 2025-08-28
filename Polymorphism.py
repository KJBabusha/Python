# demonstrating Polymorphism with move() as method
class Animal:
    def move(self):
        print("animals move by walking ")

class Automobile:
    def move(self):
        print("Automobile move by driving")

class Aircraft:
    def move(self):
        print("Aircraft moves by flying")

# objects of different kinds
object = [Animal(), Automobile(), Aircraft()]

#polymorphism in Action
for obj in object:
    obj.move()

