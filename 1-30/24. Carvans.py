for _ in range(int(input())):
    n = int(input())
    lis = [int(x) for x in input().split()]
    count = 1
    start = lis[0]
    if n == 1:
        print(1)
    else:
        for i in range(1, n):
            if start >= lis[i]:
                count += 1
                start = lis[i]
        print(count)