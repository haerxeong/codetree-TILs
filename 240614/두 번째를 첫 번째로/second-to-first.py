string = input()
first, second = string[0], string[1]
for s in string:
    if s == second:
        print(first, end = '')
    else: print(s, end = '')