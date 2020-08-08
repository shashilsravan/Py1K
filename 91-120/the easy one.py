from collections import Counter

v = pow(10, 9) + 7
arr = [1, 1]
for i in range(2, pow(10, 5) + 1):
    arr.append((arr[-1] * i) % v)
t = int(input())
for i in range(t):
    s = input()
    c = Counter(s)
    prod = 1
    for item in c.values():
        prod *= arr[item]
        prod = prod % v
    print((arr[len(s)] * pow(prod, v - 2, v)) % v)