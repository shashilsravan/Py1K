for _ in range(int(input())):
    n = int(input())
    lis = [int(x) for x in input().split()]
    lis.sort()
    print(min([lis[i]^lis[i+1] for i in range(n-1)]))