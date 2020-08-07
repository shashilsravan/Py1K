def getSum(arr, a, b):
    if a == b:
        return arr[b]
    return arr[b] - arr[a]


arr = [1, 2, 3, 4, 5, 6, 7]
myArr = [0] * len(arr)
myArr[0] = arr[0]
for i in range(1, len(arr)):
    myArr[i] = myArr[i-1] + arr[i]
print(myArr)
print(getSum(myArr, 0, 3))
print(getSum(myArr, 1, 3))