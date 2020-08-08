from collections import Counter
n = int(input())
lis = [int(x) for x in input().split()]
count = Counter(lis)
print(sum(sorted(list(count.values()), reverse=True)[1:]))