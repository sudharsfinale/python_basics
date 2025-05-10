def multiply(*numbers):
    # here numbers is a tuple
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 3, 4, 5))
