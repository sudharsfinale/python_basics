if __name__ == '__main__':
    N = int(input("Enter "))
    arr = []

    for _ in range(N):
        command = input("Enter the array command : ").split()
        operation = command[0]

        if operation == 'insert':
            index = int(command[1])
            value = int(command[2])
            arr.insert(index, value)
        elif operation == 'print':
            print(arr)
        elif operation == 'remove':
            value = int(command[1])
            arr.remove(value)
        elif operation == 'append':
            value = int(command[1])
            arr.append(value)
        elif operation == 'sort':
            arr.sort()
        elif operation == 'pop':
            arr.pop()
        elif operation == 'reverse':
            arr.reverse()
    print(arr)