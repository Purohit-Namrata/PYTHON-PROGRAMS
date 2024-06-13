
#DOUBT
class MyClass:
    x=5
    def myfunc(self,c):
        y=c
        print(c)
        
        print("This is myclass function")
        

p1=MyClass()
print(p1.x)

print (p1.myfunc(95))
#print('abc')
#p1.x=9
#print(p1.x)

'''

class MathOperations:
    def testAddition (self,x, y):
        return x + y
    def testMultiplication (self,a, b):
        return a * b

tmp = MathOperations()
print (tmp.testAddition(2,3))




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
#print(p1)
#print(p1.name)
#print(p1.age)



#DOUBT

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)






class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is " ,self.name)

p1=Person("John",36)
p1.myfunc()



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40
p1.name='jojo'

print(p1.name)

'''











