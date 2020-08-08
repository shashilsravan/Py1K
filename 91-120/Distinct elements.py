# O(n) approach
arr = [1, 2, 1, 3, 2, 4, 4, 2, 3, 5]
res = {}
for a in arr:
    res[a] = 1
print(len(res))
# or
# print(len(set(arr))