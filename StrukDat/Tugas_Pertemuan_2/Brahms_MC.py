n = int(input())  # Total input
a = list(map(int, input().split()))  # Guest input

temp = ["temp"] * n  # Array with temporary member
a = a + temp


for i in range(n):
    itr = i  # Increment
    
    if a[itr] == a[itr+1] and a[itr] != "temp":  # If duplicate
        a.pop(itr)
        a.pop(itr)
        
        if itr == 0 or 1:  # Adjusting the index
            itr = 0
        else:
            itr = itr - 2


for j in temp:  # Remove all temp
    a.pop()

catering = len(set(a))  # Count only the different members
print(catering)
