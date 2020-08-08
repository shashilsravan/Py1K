for _ in range(int(input())):
    string = input()
    n = len(string)//2
    acost = int(input())
    bcost = int(input())
    lis1 = [string[i] for i in range(n)]
    lis2 = list(reversed([string[i] for i in range(n, len(string))]))
    cost = 0
    for i in range(n):
        if lis1[i] == '/':
            if lis2[i] == 'a':
                cost += acost
            elif lis2[i] == 'b':
                cost += bcost
            else:
                if acost < bcost:
                    cost += 2 * acost
                else:
                    cost += 2 * bcost
        elif lis2[i] == '/':
            if lis1[i] == 'a':
                cost += acost
            elif lis1[i] == 'b':
                cost += bcost
        else:
            pass
    print(cost if cost > 0 else -1)