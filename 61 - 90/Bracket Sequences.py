string = input()
p = 0
t = 0
res = 0
for s in string:
    if s == '(':
        p += 1
    else:
        p -= 1
    if p < t:
        t = p
        res = 0
    if t == p:
        res += 1
if p:
    print(0)
else:
    print(res)