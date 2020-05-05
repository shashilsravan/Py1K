for _ in range(int(input())):
    for __ in range(int(input())):
        a, b, c = map(int, input().split())
        temp = pow(-1, b+1)
        if temp == 1:
            if a == c:
                print(b//2)
            else:
                print(b - b//2)
        else:
            if a == c:
                print(b - b//2)
            else:
                print(b//2)

# hhhhh - thhhh - hthhh - ththh - hthth - ththt - hhtht