# Here 1 is a default value , if we specify value from result, it will take that or by default it will take 1
# def increment(number, by=1, another): # Non-default argument follows default argument
def increment(number, by=1):
    return number + by


result = increment(2)
print(result)  # Output: 3
