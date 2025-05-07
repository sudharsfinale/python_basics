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
