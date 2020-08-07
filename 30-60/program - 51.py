MAX = 1000000

def maxOccuredElement(L, R, n):
    arr = [0] * MAX
    ind = 0
    for i in range(n):
        arr[L[i]] += 1
        arr[R[i] + 1] -= 1
    msum = arr[0]
    for i in range(1, MAX):
        arr[i] += arr[i - 1]
        if msum < arr[i]:
            msum = arr[i]
            ind = i
    return ind

print(maxOccuredElement([1,2,3], [3,5,7], 3))