class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

animals = [Dog(), Bird()]
for animal in animals:
    animal.move()
