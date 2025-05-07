for number in range(3):
    # here number will be the index
    # in js for (let i = 0; i < 3; i++) {}
    print("Hello bro", number, (number + 1) * ".")
for number in range(1, 3):
    # here number will be the index
    # in js for (let i = 1; i < 3; i++) {}
    print("Hello bro", number, number * ".")
for number in range(1, 10, 2):
    # here number will be the index
    # in js for (let i = 1; i < 10; i+=2) {}
    print("Hello bro", number, number * ".")

successful = False
# for else
for number in range(1, 4):
    print("Attempt")
    if successful and number == 2:
        print("Successful at 2")
        break
else:
    # comes to this block only if the for loop doesn't break earlier
    print("Not successful")

# nested loops

for i in range(5):
    for j in range(3):
        print(f"({i}, {j})")  # f-string
