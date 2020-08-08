res = {}
str1 = input()
str2 = input()

# O(2n)
# for s in str1:
#     if s in res:
#         res[s] += 1
#     else:
#         res[s] = 1
# for s in str2:
#     if s in res and res[s] > 0:
#         res[s] -= 1
#     else:
#         print('No')
#         break
# else:
#     print('Yes')

count = [0]*26
for i in range(len(str1)):
    count[ord(str1[i]) - 97] += 1
for i in range(len(str2)):
    count[ord(str2[i]) - 97] -= 1
print('Yes' if count.count(0) == 26 else 'No')
# print(count)