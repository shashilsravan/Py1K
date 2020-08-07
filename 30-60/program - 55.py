for _ in range(int(input())):
    num = int(input())
    a, b, c = 1, 2, 3
    even_sum = 2
    while c < num:
        if c % 2 == 0:
            even_sum += c
        a, b, c = b, c, b + c
    print(even_sum)
