count = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a/10000000000
    b = b/10000000000
    div1 = a/b
    div2 = b/a
    if 1.6 <= div1 <= 1.7 or 1.6 <= div2 <= 1.7:
        count += 1
print(count)