string = input()
target1, target2 = string[0], string[1]
for s in string:
    if s == target1:
        print(target2, end = '')
    elif s == target2:
        print(target1, end = '')
    else: print(s, end = '')