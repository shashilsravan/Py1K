MAX = 256
count = [0] * (MAX + 1)


def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)


def populate(string):
    for i in range(len(string)):
        count[ord(string[i])] += 1
    for i in range(1, MAX):
        count[i] += count[i - 1]


def update(ch):
    for i in range(ord(ch), MAX):
        count[i] -= 1


def findRank(string):
    len1 = len(string)
    mul = fact(len1)
    rank = 1
    populate(string)
    for i in range(len1):
        mul = mul // (len1 - i)
        rank += count[ord(string[i]) - 1] * mul
        update(string[i])
    return rank


print(findRank('abc'))
