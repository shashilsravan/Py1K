from collections import Counter
int(input())
a = list(map(int, input().split()))
k = int(input())
print(min(filter(lambda x: x[1] == k, Counter(a).items()))[0])