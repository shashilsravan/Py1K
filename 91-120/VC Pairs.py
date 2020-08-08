lis = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
    n = int(input())
    string = input()
    count = 0
    for i in range(n-1):
        if (string[i] not in lis) and (string[i+1] in lis):
            count += 1
    print(count)

# or
# import re
# for _ in range(int(input())):
#     n = int(input())
#     string = input()
#     print(len(re.findall(r'[^aeiou][aeiou]', string)))