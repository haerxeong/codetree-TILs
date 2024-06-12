input_string = input()
target = input()
ans = 0

for i in range(len(input_string) - len(target)):
    if input_string[i:i+len(target)] == target:
        ans = i
        break

print(ans if target in input_string else -1)