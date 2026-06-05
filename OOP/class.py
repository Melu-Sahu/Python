

class Dog:
    def __init__(self, name, breed, color):   # __init__ method runs only once when object is created
        self.name = name
        self.breed = breed
        self.color = color

    def color(self):  # Every standard method inside a class needs self as its first parameter.
        print(self.color)

    @staticmethod
    def sound(): # No 'self' needed here anymore! Because it's static method
        print("Woof Woof")


d1 = Dog('Parker', 'Indian', 'Black')


print(d1.name)
print(d1.color)

d1.sound()
