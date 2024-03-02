plates = []  # Array for the plates

def add_plate(x, y):  # Function for the commands
    for _ in range(y):
        plates.append(x)

def del_plate(x):
    for _ in range(x):
        plates.pop()

def adx_plate(x):
    i = 0
    for _ in plates:
        plates[i] = plates[i] + x
        i += 1

def dex_plate(x):
    i = 0
    for _ in plates:
        plates[i] = plates[i] - x
        i += 1

def mux_plate(x):
    i = 0
    for _ in plates:
        plates[i] = plates[i] * x
        i += 1


N = int(input())  # Amount of commands

plate_check = []  # Array for checking the plates

for i in range(N):
    command = input().split()
    z = command[0]
    x = int(command[1])
    if len(command) == 3: y = int(command[2])  # For "add" command

    if z == "add":
        add_plate(int(x), int(y))
        plate_check.append(len(plates))  # To check
    elif z == "del":
        plate_check.append(plates[-1])  # To check
        del_plate(int(x))
    elif z == "adx":
        adx_plate(int(x))
    elif z == "dex":
        dex_plate(int(x))
    elif z == "mux":
        mux_plate(int(x))


loop = 0
for j in plate_check:  # Print the checking result
    print(plate_check[loop])
    loop += 1  # Increment