import re

n = int(input())

for _ in range(n):
    k, s = input().split()
    k = int(k)

    if k == 1:
        small_letter = min(s)
        i = [m.start() for m in re.finditer(small_letter, s)]
        temp = s
        for j in i:
            s_temp = s[j:] + s[:j]
            if (s_temp < temp):
                temp = s_temp
        print(temp)

    else:
        s = list(s)
        s.sort()
        s = ''.join(s)
        print(s)