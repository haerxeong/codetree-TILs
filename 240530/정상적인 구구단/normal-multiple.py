for i in range(1, 4): 
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}", end="")
        if j < 3:
            print(",", end=" ")
    print()