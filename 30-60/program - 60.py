# Coins distribution
n = int(input())
five = (n - 4) // 5
if (n - five)% 2 == 0:
    one = 2
else:
    one = 1

two = (n - (five*5) - one)//2

print(five+two+one, five, two, one)