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


class Goa():
    name = ""

    def party(self):
        print(f"{self.name} Lets party")

    def beach(self):
        print("Lets visit beaches")


ramesh = Goa()
ramesh.name = "Ramesh"

"""
What’s happening:

1) Goa(): This calls the constructor of the Goa class. Since no __init__ method is explicitly defined, Python uses the default constructor, which initializes a new instance of the Goa class.

2) ramesh = ...: This assigns the newly created object (an instance of the Goa class) to the variable ramesh.

So in plain terms:

You're creating an object of the Goa class and naming it ramesh. This object can now call the methods defined in the class, like:
"""
suresh = Goa()
suresh.name = "Suresh"
print(ramesh.name)
print(suresh.name)
ramesh.party()
suresh.beach()


# class Laptop:
#     price = ""
#     processor = ""
#     ram = ""


# HP = Laptop()
# HP.price = "100000"
# HP.processor = "Intel"
# HP.ram = "16GB"
# print(HP.price)

class Laptop:
    # init is a inbuilt python fn called as constructor ~ A constructor is a unique function that gets called automatically when an object is created of a class.
    # uses - whenever we create a object for class, these objects should be stored in our computer memory
    """
    What is a constructor ?
    A constructor is a special function in a class that runs automatically when you create an object. Its job is to initialize the object with specific values.
    💡 In Theory: Constructor and Memory Allocation
       In lower-level languages like C++, constructors are more directly tied to memory allocation, because objects are often stored in memory in a more manual way.
       But in high-level languages like JavaScript and Python:
       The constructor doesn't directly allocate memory — the interpreter or runtime does that automatically.
       However…
       The constructor does prepare the object by assigning values to it.
       That means it indirectly triggers memory allocation because new properties are being created on a new object.
    """
    # self ~ an keyword used to denote a current object

    def __init__(self, price, processor, ram):
        self.price = price
        self.processor = processor
        self.ram = ram
        print("Constructed the values")


HP = Laptop("100000", "Intel", "16GB")
Dell = Laptop("20000", "AMD", "8gb")
print(HP.price)  # This will print "100000"


class Car:
    def __init__(self, car_name, car_model):
        self.car_name = car_name
        self.car_model = car_model

    def display(self):
        print(self.car_model)


lexus = Car("Lexus", "G73")
# This will print "G73" and then "G73" again - in background lexus.display(lexus)
lexus.display()


class Student:
    def __init__(self):
        self.student_name = ""
        self.student_age = 0

    def display(self):
        print(f"Student Name : {self.student_name}")
        print(f"Student Age : {self.student_age}")


student_1 = Student()
student_2 = Student()

student_1.student_name = "Ram"
student_1.student_age = 20

student_2.student_name = "Lakshman"
student_2.student_age = 19

student_2.display()
student_1.display()


class Fruit:
    def __init__(self, fruit_color):
        self.fruit_color = fruit_color

    def display(self):
        print(f"Fruit color : {self.fruit_color}")


apple = Fruit(fruit_color="red")
banana = Fruit(fruit_color="yellow")
apple.display()
banana.display()


class Teacher:
    relation = "Sister"

    def __init__(self, teacher_name, register_no):
        # here self is a instance variable, because self referring to an object which differs from object to object
        # variables inside constructors are called instance variable
        self.teacher_name = teacher_name
        self.register_no = register_no

    def display(self):
        print(f"Teacher Name : {self.teacher_name}")
        print(f"Teacher Register No : {self.register_no}")
        print(f"Relation : {self.relation}")


Teacher.relation = "Akka"
t1 = Teacher("Harini", "123")
t2 = Teacher("Yonisha", "456")

t1.display()
t2.display()  # Output: Teacher Name : Yonisha Teacher Register No : 456


class Calculator:
    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2

    def add(self):
        print(self.variable1 - self.variable2)

    def subtract(self):
        print(self.variable1 - self.variable2)

    def multiply(self):
        print(self.variable1 * self.variable2)

    def divide(self):
        print(self.variable1 // self.variable2)


calculator = Calculator(10, 2)
# calculator.add(12, 12)
calculator.subtract()
calculator.multiply()
calculator.divide()
