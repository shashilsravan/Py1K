for _ in range(int(input())):
    s = list(input())
    if (len(s) % 2) == 0:
        print("YES" if sorted(s[:len(s) // 2]) == sorted(s[len(s) // 2:]) else "NO")
    else:
        print("YES" if sorted(s[:len(s) // 2]) == sorted(s[len(s) // 2+1:]) else "NO")