class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"my name is {self.name} and I am {self.age} years old")

p = Person("john",30)
p.greet()