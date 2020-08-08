n = int(input())
lis = [int(x) for x in input().split()]
lis2 = [int(x) for x in input().split()]
numerator = 0
for i in range(n):
    numerator += lis[i] * lis2[i]
print('{0:.1f}'.format(numerator/sum(lis2)))