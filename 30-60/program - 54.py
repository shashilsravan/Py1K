# sum of n = n * (n + 1) // 2
# sum of 3n = 3 (n * (n + 1) // 2)
for _ in range(int(input())):
    num = int(input())
    threes = (num - 1) // 3
    fives = (num - 1) // 5
    fifteens = (num - 1) // 15
    total = (3 * threes * (threes + 1))// 2
    total = total + (5 * (fives * (fives + 1))) // 2
    total = total - (15 * (fifteens * (fifteens + 1)))// 2
    print(total)