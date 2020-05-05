a, b = map(int, input().split())
lis = sorted([int(x) for x in input().split()])
temp = []
for i in range(0, a, b):
    t = lis[i:i+b]
    if len(t) == b:
        temp.append(t)
    else:
        temp[-1] += t
total = 0
for i in range(1, len(temp) + 1):
    total += (sum(temp[i - 1]) * i)
    print(total % (pow(10, 9) + 7))