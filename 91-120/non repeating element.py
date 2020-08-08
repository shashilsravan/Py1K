res = [0] * 26
str1 = input()

for s in str1:
    res[ord(s) - 97] += 1

for s in str1:
    if res[ord(s) - 97] == 1:
        print(s)
        break