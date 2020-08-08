n = int(input())
lis = [int(x) for x in input().split()]
mean = sum(lis)/n
newlis = [pow(l-mean, 2) for l in lis]
print('{0:.1f}'.format(pow(sum(newlis)/n, 1/2)))