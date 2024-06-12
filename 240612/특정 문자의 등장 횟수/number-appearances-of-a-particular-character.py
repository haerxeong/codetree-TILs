s = input()

count_ee = sum(1 for i in range(len(s)-1) if s[i:i+2] == 'ee')
count_eb = s.count('eb')

print(count_ee, count_eb)