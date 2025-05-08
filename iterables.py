print(type(5))  # primitive types like Numbers Strings and Booleans

# complex types example is range but there are plenty of complex types out there
print(type(range(5)))

# range object is iterable which means we can iterate over it or use it in a for loop

for x in range(5):
    print(x)

# string also iterable
for x in "hello":
    print(x)

# in python => Lists [0, 1, 2, 3] | in js => Array [0, 1, 2, 3]

my_list = [1, 2, 3, 4, 5]

for x in my_list:
    print(x)
