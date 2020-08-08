d, e, f = map(int, input().split())
a, b, c = map(int, input().split())

if c < f and c != f:
    print(10000)
elif c > f or (a > d and b == e and f == c) or (b > e and f == c):
    print(0)
elif b != e:
    print(abs(b - e) * 500)
else:
    print(abs(a - d) * 15)