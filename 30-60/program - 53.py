m,n = map(int, input().split())
lis = [int(x) for x in range(1, m + 1)]
for _ in range(n):
    temp = int(input())
    if lis.count(temp) >= 1:
        lis[0], lis[-1] = lis[-1], lis[0]
    else:
        lis.pop()
        lis.append(temp)
    print(sum(lis))