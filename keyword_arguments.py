def increment(number, by):
    return number + by


# Here 2 is an argument but by=1 is a keyword argument
result = increment(2, by=1)
print(result)  # Output: 3
