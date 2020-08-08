n = int(input())
a = list(map(int, input().split()))
diff = len(set(a))
if diff == 1:
    print(int((n * (n + 1)) / 2))
elif diff == n:
    print(1)
else:
    i = j = ans = 0
    ahead = True
    distinct = {}
    while j < n:
        if ahead:
            distinct[a[j]] = distinct[a[j]] + 1 if a[j] in distinct else 1
            if len(distinct) == diff:
                ahead = False
            else:
                j += 1
        else:
            ans += n - j
            if distinct[a[i]] > 1:
                distinct[a[i]] -= 1
            else:
                distinct.pop(a[i])
                j += 1
                ahead = True
            i += 1
    print(ans)