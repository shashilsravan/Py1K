from bisect import bisect_left
from itertools import accumulate
n = int(input())
lis = list(accumulate(map(int,input().split())))
for _ in range(int(input())):
    temp = int(input())
    print(bisect_left(lis, temp)+1 if bisect_left(lis, temp)+1 <= n else -1)