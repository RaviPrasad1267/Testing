# Multipule inheri

class Animal:          # Parent1
    def eat(self):
        print("Eating...")

class Dog:          #Parent 2
    def bark(self):
        print("Barking...")

class Cat(Dog,Animal):     #Child 1
    def Catsound(self):
        print("MYvoo Myvoo...")


c = Cat()    # Crate a object
 a = Animal()
c.eat()
c.bark()
c.Catsound()



# MultiLevel

# class Animal:          # Parent1
#     def eat(self):
#         print("Eating...")
#
# class Dog(Animal):          #Child1
#     def bark(self):
#         print("Barking...")
#
# class Cat(Dog):     #Child 2
#     def Catsound(self):
#         print("MYvoo Myvoo...")
#
# c = Cat()    # Crate a object
# # a = Animal()
# c.eat()
# c.bark()
# c.Catsound()


# Hierrical

class Animal:          # Parent1
    def eat(self):
        print("Eating...")

class Dog(Animal):          #Child1
    def bark(self):
        print("Barking...")

class Cat(Animal):     #Child 2
    def Catsound(self):
        print("MYvoo Myvoo...")

c = Cat()    # Crate a object
# a = Animal()
c.eat()
d = Dog()
d.bark()
c.Catsound()




