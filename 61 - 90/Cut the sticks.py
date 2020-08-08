int(input())
lis = [int(x) for x in input().split()]
while len(lis) > 0:
    print(len(lis))
    mini = min(lis)
    lis = [l-mini for l in lis if l-mini > 0]