F = {}

for aa0 in range(10):
    for aa1 in range(10):
        for cc in range(10):
            for xx in range(41):
                a0 = aa0
                a1 = aa1
                c = cc
                x = xx
                for i in range(256):
                    a0, a1 = a1, (a0 + c * a1) % 10
                    x = (10 * x + a1) % 41
                F[(aa0, aa1, cc, xx)] = (a0, a1, c, x)

num_probs = int(input())
for prob in range(num_probs):
    a0, a1, c, n = (int(x) for x in input().split())
    if n == 1:
        print("YES" if a0 == 0 else "NO")
        continue
    x = (10 * a0 + a1) % 41

    steps = n - 2
    Q = (a0, a1, c, x)
    for _ in range(steps // 256):
        Q = F[Q]
    a0, a1, c, x = Q
    for _ in range(steps % 256):
        a0, a1 = a1, (a0 + c * a1) % 10
        x = (10 * x + a1) % 41
    print("YES" if x == 0 else "NO")