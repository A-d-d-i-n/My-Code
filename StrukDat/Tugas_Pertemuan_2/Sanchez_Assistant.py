stack = []

while True:  # Neverending, unless stopped
    inpt = input()
    if inpt == "stop":
        break

    N = list(map(str, inpt.split("/")))

    itr_i = 0  # If "N[itr_i]" -> "i" then "itr_i" is unnecessary
    for i in N:
        if N[itr_i] not in(".", "", ".."):  # If files/directory names
            stack.append(N[itr_i])

        elif N[itr_i] == ".." and stack:  # If the stack got member(s)
            stack.pop()

        itr_i += 1


res = "/" + "/".join(stack)  # Output format
print(res)