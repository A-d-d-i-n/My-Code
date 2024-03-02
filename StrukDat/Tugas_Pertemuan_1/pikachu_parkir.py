n = int(input())  # Test case
res = []  # Test case results

for I in range(n):
    y,x = map(int, input().split())  # Pikachu's arrival & parking lot slots
    j = int(input())  # Other vehicle at parking lot
    empty_slot = x - j  # Slot - vehicle

    for J in range(j):
        m,k = map(int, input().split())  # Arrival & departure times
        if y not in range(m, k):  # If the slot is empty
            empty_slot += 1
    
    if empty_slot > 0:  # Result
        res.append("Pika Pika!")
    else:
        res.append("Pika Zzz")

while len(res) != 0:
    print(res.pop(0))  # Print all results