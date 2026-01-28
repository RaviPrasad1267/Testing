class AddTwo:
    def add(self, a, b):
        return a + b   # adds two numbers


class AddThree:
    def add(self, a, b, c):
        return a + b + c   # adds three numbers


# Polymorphism in action
def perform_addition(obj):
    # same method name "add" works differently based on object
    print(obj.add(10, 20))  # works for two-argument version


# Create objects
two = AddTwo()
three = AddThree()

# Using the class with two numbers
print("Addition using AddTwo:", two.add(10, 20))

# Using the class with three numbers
print("Addition using AddThree:", three.add(10, 20, 30))


# Method Overloading
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(2))        # 2
print(m.add(2, 3))     # 5
print(m.add(2, 3, 4))  # 9


# Method Overriding

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Dog()
a.sound()   # Bark
