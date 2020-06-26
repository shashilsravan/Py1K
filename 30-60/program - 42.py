for _ in range(int(input())):
    num = int(input())
    i = 0
    while True:
        if num < pow(2, i):
            print(i)
            break
        i += 1