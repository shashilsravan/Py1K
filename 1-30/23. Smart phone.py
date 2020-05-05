lis = []
n = int(input())
for _ in range(n):
    lis.append(int(input()))
lis.sort()
price = lis[0] * n
for i in range(1, n):
    n -= 1
    price = max(price, lis[i]*n)
print(price)

# 3 21 33 40 65
# 15 84 99 80 65