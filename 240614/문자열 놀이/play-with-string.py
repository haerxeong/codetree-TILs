s, q = input().split()
s = list(s)

for _ in range(int(q)):
    command = input().split()
    
    if command[0] == '1':
        # Swap the characters at positions given by command[1] and command[2]
        idx1 = int(command[1]) - 1
        idx2 = int(command[2]) - 1
        s[idx1], s[idx2] = s[idx2], s[idx1]
    else:
        # Replace occurrences of command[1] with command[2]
        old_char = command[1]
        new_char = command[2]
        s = [new_char if char == old_char else char for char in s]
    
    print(''.join(s))  # Convert list back to string for printing