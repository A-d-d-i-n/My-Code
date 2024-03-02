N = int(input())  # Dirty plates

plat_dir = list(range(N+1))  # Array of dirty plates (bottom to top)
plat_dir.pop(0)
plat_dir.reverse()

plat_lat = []  # Array for lathered plates
plat_cle = []  # Array for clean plates

M = int(input())  # Activities


for i in range(M):
    C,D = map(int, input().split())  # Role & stack of plates

    if C == 1:  # If Dede / lathering the plates
        if D >= len(plat_dir): D = len(plat_dir)
        
        for j in range(D):
            plat_lat.append(plat_dir[-1])
            plat_dir.pop()
    
    elif C == 2:  # If his friend / washing the plates
        if D >= len(plat_lat): D = len(plat_lat)
        
        for k in range(D):
            plat_cle.append(plat_lat[-1])
            plat_lat.pop()


plat_dir.reverse() # Bottom-to-top -> top-to-bottom
if len(plat_dir) == 0: plat_dir.append("-")  # "-" = no plates/empty
plat_lat.reverse()
if len(plat_lat) == 0: plat_lat.append("-")
plat_cle.reverse()
if len(plat_cle) == 0: plat_cle.append("-")


plat_max = int(max(len(plat_dir), len(plat_lat), len(plat_cle)))  # Stack with the most plates


print(plat_dir[0], "\t", plat_lat[0], "\t", plat_cle[0])

loop = 1  # The top is already printed

for l in range(plat_max - 1):  # The top is aready printed
    if (plat_dir[0] == "-") and (plat_lat[0] == "-") and (plat_cle[0] == "-"):  # If 3 stacks empty
        print(" ", "\t", " ", "\t", " ")


    elif (plat_dir[0] == "-") and (plat_lat[0] == "-"):  # If 2 stacks empty
        print(" ", "\t", " ", "\t", plat_cle[loop])

    elif (plat_dir[0] == "-") and (plat_cle[0] == "-"):
        print(" ", "\t", plat_lat[loop], "\t", " ")
    
    elif (plat_lat[0] == "-") and (plat_cle[0] == "-"):
        print(plat_dir[loop], "\t", " ", "\t", " ")
    

    elif plat_dir[0] == "-":  # If 1 stack empty
        print(" ", "\t", plat_lat[loop], "\t", plat_cle[loop])
    
    elif plat_lat[0] == "-":
        print(plat_dir[loop], "\t", " ", "\t", plat_cle[loop])

    elif plat_cle[0] == "-":
        print(plat_dir[loop], "\t", plat_lat[loop], "\t", " ")


    else:  # If none of them are empty
        print(plat_dir[loop], "\t", plat_lat[loop], "\t", plat_cle[loop])


    loop += 1  # Increment