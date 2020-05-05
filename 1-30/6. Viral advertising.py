from itertools import accumulate
shared = [5, ]
liked = []
n = int(input())
for i in range(n):
    liked.append(shared[i]//2)
    shared.append(liked[i] * 3)
cummulative = list(accumulate(liked))
print(cummulative[n - 1])