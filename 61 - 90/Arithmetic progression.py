import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(0 if b-a == c-b else math.ceil(abs(2*b-c-a)/2))