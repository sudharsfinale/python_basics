# Conditional Statements ~ used when it is a time to take decisions
temperature = 33
# if and else
if temperature > 34:
    # indentation is necessary to make understand the python interpreter to what statements should be executed if the condition passes
    print("It is hot")
else:
    print("It is not hot")

# if elif else
if temperature > 34:
    print("It is hot")
elif temperature > 18:
    print("It is medium hot")
elif temperature > 4:
    print("It is cold")
else:
    print("It is very cold")
