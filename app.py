# starter code ~ Sudharsan (May 5, 2025)
# imports
import math
# print is more like a console.log in js to print output
print("Hello World")
# expression ~ Expression is a piece of code that returns a value
print("*" * 10)

# beautiful code according to Python Enhancement Proposals ~ Refer: PEP 8 – Style Guide for Python Code
x = 7

# variables
# We use variables to store data in computer’s memory, Ex: students_count = 1000 => when we run this program, python interpreter will allocate some memory and store this number thousand in that memory space,
students_count = 1000


# What kind of data we can store in computers memory ?
# - We have several kinds of data, Some builtin primitive data types are Numbers, Booleans and Strings

# ~ 1. Numbers
# a) Whole Number / integer in programming
blogs_count = 100
# b) Float / Floating point number ~ more like a decimal number
blog_rating = 4.5

# ~ 2. Booleans
# Boolean is a primitive data type that can have only two values: True or False ~ These are most likely used in taking decisions
is_published = True
is_published = False

# ~ 3.String ~ A sequence of characters, like a sentence or a word
course_name = "Python Programming"

# Tip ~ from we learned so far
# 1. all variable names should be descriptive and meaningful
# 2. all variable names should be in lowercase
# 3. all variable names should be separated by underscore if it is a multi word variable name
# 4. all variable names should not start with a number
# 5. all variable names should have space around the equal sign (pep 8)


# Some useful things to do with string
# 1) triple quote ~ mostly used in mail templates
message = """
    Hi Sudharsan, 

    Vanakkam bro from Bangalore

    Blah blah blah
"""

# Function ~ It is a reusable piece of code that carries out a task
# Function is a block of code that can be called multiple times from different parts of the program

# String functions

string = "Hi there lets try length of the string"
print(len(string))  # length of the string
# accessing first element from the string with bracket notations
print(string[0])
print(string[-1])  # accessing last element from the string
print(string[0:5])  # accessing a part of the string more like a slice
print(string[:])  # this gives the exact copy of our string


# Escape Sequences
# how to write python "programming"
print('python "programming"')
print("python \"programming\"")
print("python \nprogramming")  # new line \n
print("python \tprogramming")  # tab \t

# Formatted Strings

# concatenation approach
first_name = "Sudharsan"
last_name = "R"
full_name = first_name + " " + last_name
# formatted string approach
# this is more like `${first_name} ${last_name}` in js
full_name = f"{first_name} {last_name}"
print(full_name)

# String Methods ~ more like a few available fn to work with strings
course = "Python programming"
# all these methods create a copy of the original string that is it wont affect the actual string
print(course.lower(), "~ lower")  # convert string to lowercase
print(course.upper())  # convert string to uppercase
print(course.capitalize())  # capitalize the first letter of the string
print(course.title())  # capitalize the first letter of each word in the string
print(course.split())  # split the string into a list of words
print(course.replace("pro", "Pro"))  # replace a word in the string
# remove the leading and trailing spaces from the string, more like a trim in js
print(course.strip())
# used to check whether the char or sequence of char is not in string or not
print("prod" not in course)
# used to check whether the char or sequence of char is in string or not
print("prod" in course)

# Numbers

# Integers ~ Integers are whole numbers, either positive, negative, or zero
integer_number = 1000
# Floating Numbers or Floating point numbers ~ more like a decimal number
float_number = 1.1
# Complex Numbers ~ more like a number with real and imaginary part
complex_number = 1 + 2j

# Arithmetic operations
print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # division
print(71 // 12)  # floor division
print(10 % 3)  # modulus
print(10 ** 3)  # exponentiation

# Augmented assignment operator
# more like a shorthand for the above arithmetic operations
x = 10
x += 3  # more like x = x + 3
x -= 3  # more like x = x - 3
x *= 3  # more like x = x * 3
x /= 3  # more like x = x / 3

# Working with Numbers

# builtin functions
print(round(2.9))  # Rounds to nearest integer (standard)
print(abs(-2.9))  # Returns positive version of the number
# functions from math module ~ here math is a object so that we can access its methods like we access from the object
print(math.ceil(2.2))  # Output: 3 ~ Rounds up to nearest integer
print(math.floor(2.9))  # Output: 2 ~ Rounds down to nearest integer
print(math.factorial(5))  # Output: 6 ~ Returns factorial of the number

# Type conversion
# str
print(str(123))  # Output: "123"
# int
print(int("123"))  # Output: 123
# float
print(float("123"))  # Output: 123.0
# bool
print(bool(1))  # Output: True
# Falsy bool values
print(bool(0))  # Output: False
print(bool(""))  # Output: False
print(bool([]))  # Output: False
print(bool({}))  # Output: False
print(bool(None))  # Output: False
# Truthy bool values
print(bool(1))  # Output: True
print(bool("Hello"))  # Output: True
print(bool([1, 2, 3]))  # Output: True
print(bool({1, 2, 3}))  # Output: True
print(bool((1, 2, 3)))  # Output: True
