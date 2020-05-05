for _ in range(int(input())):
    num = int(input())
    count = 0
    i = 1
    while int(num/pow(5, i)) != 0:
        count += int(num/pow(5, i))
        i += 1
    print(count)