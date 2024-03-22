n = int(input())  # Total of fish
i = list(map(int, input().split()))  # The fishes 

""" i must be consecutive and cannot contain dupes """

to_print = []
pending = []


while i:  # Won't stop 'till i ran out of member
    if i[0] != max(i):
        pending.append(i.pop(0))
        print()

    else:
        to_print.append(i.pop(0))

        itr = 0
        for j in range(len(pending)):
            pending.sort(reverse = True)  # Big --> small

            if pending[itr] == to_print[-1] - 1:  # If one from the pending is the next to to_print
                to_print.append(pending.pop(itr))
            else:
                itr += 1
        
        print(" ".join(map(str, to_print)))  # Output format
        to_print = []

