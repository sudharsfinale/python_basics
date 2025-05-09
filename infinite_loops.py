# to jump out of a infinite loop we need to break that after meeting certain condition

while True:

    print("Type q to quit")

    user_input = input("Type anything: ")

    if (user_input.lower() == "q"):
        break
