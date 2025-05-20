"""
Single Level Inheritance
Explanation:
------------------------
1) Class Definition:

Dad class: It has a method called phone() that prints "Dad's Phone".

Son class: It inherits from the Dad class, which means it has access to all the methods and attributes of the Dad class. Additionally, the Son class has a method called laptop(), which prints "Son's Laptop".

2) Object Creation:

The line son = Son() creates an instance of the Son class.

3) Calling son.phone():

When son.phone() is called, Python checks if the Son class has the phone() method. Since the Son class doesn't define it, Python looks in the Dad class (the parent class) for the method.

It finds the phone() method in the Dad class and executes it, printing "Dad's Phone".


Summary:
The Son class inherits from the Dad class. When you create an instance of Son and call phone(), Python uses method inheritance and calls the phone() method from the Dad class.
"""


class Dad():
    def phone(self):
        print("Dad's Phone")


class Mom():
    def sweet(self):
        print("Mom's Sweet")

# Single Level Inheritance


class Daughter(Dad):
    def mobile(self):
        print("Son's Laptop")

# Multiple Inheritance


class Son(Dad, Mom):
    def laptop(self):
        print("Son's Laptop")


son = Son()
daughter = Daughter()
son.phone()
son.sweet()
daughter.phone()
