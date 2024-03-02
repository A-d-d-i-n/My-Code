arr =[]  # Pre-existing array

while True:  # Forever looping
    inpt = input().split()
    command = inpt[0]

    if command == "append":
        arr.append(inpt[1])

    elif command == "prepend":
        arr.insert(0, inpt[1])

    elif command == "cp":  # Copy
        arr.insert(int(inpt[2]), arr[int(inpt[1])])

    elif command == "mv":  # Move
        temp = arr[int(inpt[1])]  # Temporary variable
        arr.pop(int(inpt[1]))
        arr.insert(int(inpt[2]), temp)

    elif command == "rm":  # Remove
        arr.pop(int(inpt[1]))

    elif command == "stop":
        break  # Break the loop


print(len(arr))  # Show amount of data/member

loop = int(0)
for i in arr:
    print(arr[loop])  # Print data
    loop += 1  # Increment