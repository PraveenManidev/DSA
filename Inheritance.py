class Pet:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def show(self):
        print(f"I am {self.name} and am {self.age} years old")
    def speak(self):
        print("I dont know what to say")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color 

    def speak(self):
        print("Meow")
c = Cat("Praveen",25,'Brown')

c.speak()