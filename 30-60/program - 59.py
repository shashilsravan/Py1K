n = int(input())

for i in range(n):
    value = int(input())
    coincount = 0
    while value >= 1:
        value = value//2
        coincount += 1
    print(coincount)