class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age
        print("Hi I am from Constructor method")

    def Print121(self):      # Normal Method/Fun

        print("Hello Welcome to the Python clas")

p = Person("Alice", 25)  # __init__ runs automatically
p.Print121()    # Normal method using object

