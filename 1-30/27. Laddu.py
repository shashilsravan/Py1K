s = {
    "INDIAN":200,
    "NON_INDIAN":400,
    "CONTEST_WON":300,
    "TOP_CONTRIBUTOR":300,
    "BUG_FOUND":1,
    "CONTEST_HOSTED":50,
}
for _ in range(int(input())):
    a, b = input().split()
    total = 0
    for _ in range(int(a)):
        lis = [x for x in input().split()]
        if lis[0] in s:
            if lis[0] == 'CONTEST_WON' and int(lis[1]) <= 20:
                bonus = 20 - int(lis[1])
                total += bonus + 300
            elif lis[0] == 'CONTEST_WON' and int(lis[1]) > 20:
                total += 300
            elif lis[0] == 'BUG_FOUND':
                total += int(lis[1])
            else:
                total += s[lis[0]]
    print(total//s[b])
