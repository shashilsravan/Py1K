for _ in range(int(input())):
    a, b, c = map(int, input().split())
    t = (c + (b % a) - 1) % a
    print(t if t > 0 else a)