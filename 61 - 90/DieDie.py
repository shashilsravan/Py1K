mod = 1000000007
for _ in range(int(input())):
    print(pow(pow(2, mod - 2, mod), int(input()) - 1, mod))