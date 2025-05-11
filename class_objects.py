# Class is a design for the object
"""
| Concept      | Python           | JavaScript      |
| ------------ | ---------------- | --------------- |
| Class        | `class Dog:`     | `class Dog {}`  |
| Constructor  | `def __init__()` | `constructor()` |
| Method Call  | `dog1.speak()`   | `dog1.speak()`  |
| Instance Var | `self.name`      | `this.name`     |
"""


# How to define a Class
class Car:
    # class can contain attributes and behaviors
    # attributes are variables that are part of the class
    # behaviors are methods | functions that are part of the class
    def config(self):  # config method
        print(f"Hello from config self {self}")


print("This is a car class")
car = Car()
a = "hello"
print(type(a))  # <class 'str'> ~ str is a inbuilt class
print(type(car))  # <class '__main__.Car'> ~ Car is our class

# Everything is object in python - 1) inbuilt class 2) the classes we create

# How to access a method inside a class

Car.config(car)
