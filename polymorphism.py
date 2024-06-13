'''class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

class Prisha:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Hello")


car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class
prisha1=Prisha("Viva","montessori") 

car1.move()
boat1.move()
prisha1.move()
for x in (car1, boat1, plane1,prisha1):
  x.move()
'''

#Inheritance class polymorphism

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(slef):
        print("Vehicle move")

class Car(Vehicle):
    pass

class Bus(Vehicle):
    def move(self):
        print('Bus vehicle')

car1=Car("honda","jazz")
bus1=Bus("Volvo","bus")
car1.move()
bus1.move()

print(car1.brand)
for x in (car1,bus1):
    print(x.brand)
    print(x.model)
    x.move()


    
