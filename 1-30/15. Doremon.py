a, b = map(int, input().split(' '))
res = -b ** 2
cl = a
if a:
    for i in range(a):
        q = b // (i + 2)
        ac = (a - i) ** 2 + i
        r = b % (i + 2)
        ac -= ((i + 2) - r) * q ** 2 + r * (q + 1) ** 2
        if ac > res:
            res = ac
            cl = a - i
print(res)
if a:
    q = b // (a - cl + 2)
    r = b % (a - cl + 2)
    print('x' * q, end='')
    print('o' * cl, end='')
    print('x' * (q + (1 if r else 0)), end='')
    r = max(r - 1, 0)
    for i in range(a - cl):
        print('o', end='')
        print('x' * (q + (1 if r else 0)), end='')
        r = max(r - 1, 0)
    print("\n")
else:
    print('x' * b)
