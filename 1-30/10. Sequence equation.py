n = int(input())
lis = [int(x) for x in input().split()]
for i in range(n):
    print(lis.index(lis.index(i + 1) +1) +1)