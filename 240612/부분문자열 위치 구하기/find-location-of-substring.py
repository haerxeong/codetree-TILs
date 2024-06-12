input_string = input()
target = input()

for i in range(len(input_string) - len(target) + 1):
    if input_string[i:i+len(target)] == target:
        ans = i
        break

print(ans if target in input_string else -1)