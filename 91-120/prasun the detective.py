string1 = input().replace(" ", "")
string2 = input().replace(" ", "")
lis = [0] * 200
for i in range(len(string1)):
    if 65 <= ord(string1[i]) <= 90:
        lis[ord(string1[i])] += 1
        lis[32 + ord(string1[i])] += 1
    elif 97 <= ord(string1[i]) <= 122:
        lis[ord(string1[i])] += 1
        lis[ord(string1[i]) - 32] += 1
    else:
        lis[ord(string1[i])] += 1
flag = 1
for i in range(len(string2)):
    if lis[ord(string2[i])] >= 1:
        lis[ord(string2[i])] -= 1
    else:
        flag = 0
        break
print('YES' if flag == 1 else "NO")