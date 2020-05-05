for _ in range(int(input())):
    n = int(input())
    count = 0
    i = 1
    while int(n/pow(5, i)) != 0:
        count += int(n/pow(5, i))
        i += 1
    print(count)