def func(a, b, c):
    if a>=b:
        return ((a-b)//2 + (a-b)%2)
    elif b%c == 0:
        return (1+func(a*c, b, c))
    else:
        rem = (b//c + 1) * c
        return ((rem - b)//2 + (rem-b)%2 + func(a, rem, c))


for _ in range(int(input())):
    k, m, n = map(int, input().split())
    print(func(k, m, n))

# 11 6 2 --> 2 + 1
# 3 6 2 -->