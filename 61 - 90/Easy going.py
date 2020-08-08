from sys import stdin
for _ in range(int(stdin.readline())):
    m, n = map(int, stdin.readline().split())
    lis = [int(x) for x in stdin.readline().split()]
    diff = abs(m - n)
    lis.sort()
    print(sum(lis[m-diff:]) - sum(lis[:diff]))