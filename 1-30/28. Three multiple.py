for _ in range(int(input())):
    k, a, b = map(int, input().split())
    num = (a + b) % 10
    cycles = (k - 3) // 4
    extras = (k - 3) % 4
    c1 = (2 * a + 2 * b) % 10
    c2 = (4 * a + 4 * b) % 10
    c3 = (8 * a + 8 * b) % 10
    c4 = (6 * a + 6 * b) % 10
    if k == 6:
        c4 = 0
    elif k == 5:
        c4 = c3 = 0
    elif k == 4:
        c4 = c3 = c2 = 0
    elif k <= 3:
        c4 = c3 = c2 = c1 = 0
    else:
        pass
    n1 = c1 * cycles
    n2 = c2 * cycles
    n3 = c3 * cycles
    n4 = c4 * cycles
    if extras == 1:
        n1 = n1 + c1
    elif extras == 2:
        n1 = n1 + c1
        n2 = n2 + c2
    elif extras == 3:
        n1 = n1 + c1
        n2 = n2 + c2
        n3 = n3 + c3
    elif extras == 4:
        n1 = n1 + c1
        n2 = n2 + c2
        n3 = n3 + c3
        n4 = n4 + c4
    print('YES' if (n1 + n2 + n3 + n4 + num + a + b) % 3 == 0 else 'NO')
