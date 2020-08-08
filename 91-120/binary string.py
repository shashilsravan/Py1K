import re

A = "0100010010"
B = [
       [1, 8],
       [3, 7]
     ]

res = []
for b in B:
    first, last = b[0]-1, b[1]
    temp = A[first:last]
    pattern = r'1[01]*1'
    ans = re.search(pattern, temp)
    if ans:
        res.append(ans.group().count('0'))
    else:
        res.append(0)

print(res)