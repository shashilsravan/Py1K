for _ in range(int(input())):
    n = int(input())
    lis = [int(x) for x in input().split()]
    a = [ele-i for i, ele in enumerate(lis)]
    b = [ele+i for i,ele in enumerate(lis)]
    print(max(max(a) - min(a), max(b) - min(b)))
#     (ai + i) - (j + aj)
