a, b = map(int, input().split())
lis = []
for _ in range(a):
    lis.append(input())
ans = []
for i in range(len(lis)):
    for j in range(i+1, len(lis)):
        ans.append(bin(int(lis[i], 2) | int(lis[j], 2)).replace('0b', '').count('1'))
print(max(ans))
print(ans.count(max(ans)))