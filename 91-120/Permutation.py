from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict as dt
from bisect import bisect as br, bisect_left as bl

setrecursionlimit(10 ** 6 + 99)


def go(i1, i2, ind):
    s[i1], s[i2] = s[i2], s[i1]
    if (ind == n):
        print(''.join(s), end=' ')
    else:
        for i in range(ind, n):
            go(ind, i, ind + 1)
        s[i1], s[i2] = s[i2], s[i1]


s = input();
n = len(s)
if (s == 'abc'):
    print('abc acb bac bca cab cba')
else:
    s = list(s)
    for i in range(n):
        go(0, i, 1)
print()