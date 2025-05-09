# we always make functions reusable and make it little chunks to make them easily readable


# Two types of function

# 1 - Perform a task
def greet(first_name, last_name="", shouldReturn=False):
    if shouldReturn:
        return f"Hello, {first_name} {last_name}"
    else:
        print(f"Hi there {first_name} {last_name}")


greet("Sudharsan", "R")
# 2 - Functions that calculate and return a value

message = greet("Sudharsan", "Ravi", True)
file = open("content.txt", "w")
file.write(message)
print(message)


def noneFn():
    print("I am a function who return None")


print(noneFn())
