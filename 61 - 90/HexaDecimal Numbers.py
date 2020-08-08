import math

s = '0123456789abcdef'
dic = {x: i for i, x in enumerate(s)}
arr = [0] * 100001


def sum_digit(x, k=16):  # faster
    r = 0
    while x >= k:
        r += x % k
        x = x // k
    return r + x

for i in range(1, 100001):
    c = sum_digit(i)
    if math.gcd(i, c) > 1:
        arr[i] = 1
for i in range(1, 100001):
    arr[i] += arr[i - 1]

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(arr[r] - arr[l - 1])