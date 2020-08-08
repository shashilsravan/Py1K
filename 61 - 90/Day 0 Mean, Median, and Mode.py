# Calculating mean, mode and median of the given array
from collections import Counter
n = int(input())
lis = [int(x) for x in input().split()]
# Mean
print(sum(lis)/n)

# Median
lis = sorted(lis)
if len(lis) % 2 == 0:
    print((lis[(len(lis)//2)-1]+lis[(len(lis)//2)])/2)
else:
    print(lis[len(lis)//2])

# Mode
print(max(Counter(lis), key=Counter(lis).get))