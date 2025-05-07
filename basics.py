# starter code ~ Sudharsan (May 5, 2025)
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


# 1. Everything in Python is an object ~ Even basic things like integers, strings, lists — all of them are objects of specific classes:

# 10 → an instance of the int class

# "10" → an instance of the str class


# when using a virtual environment we have to change our interpreter from global python to current environment
"""
A virtual environment is a self-contained Python environment that allows you to isolate your project's dependencies from the system Python environment. This is useful for several reasons:

1. Avoid version conflicts: By creating a virtual environment for each project, you can ensure that the project's dependencies are installed in a specific version, without affecting the system Python environment.

2. Simplify dependency management: Virtual environments make it easier to manage dependencies for each project, as you can install and manage dependencies within the virtual environment, without affecting the system Python environment.

3. Improve reproducibility: Virtual environments help ensure that your project's dependencies are consistent across different environments, making it easier to reproduce your project's behavior.

"""
# setup
"""  from ChatGPT
✅ 4. Make sure VS Code is using the correct interpreter
In VS Code:

Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)

Type: Python: Select Interpreter

Choose the one pointing to your venv (should include the path to venv/bin/python or venv\Scripts\python.exe)
"""
