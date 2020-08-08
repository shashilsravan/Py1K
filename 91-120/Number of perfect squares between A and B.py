import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)