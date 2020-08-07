def reverse(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        high, low = high -1, low + 1
    return arr

n = int(input())
arr = [int(x) for x in input().split()]
arr1 = reverse(arr, 0, n-1)
arr2 = reverse(arr1, n, len(arr) - 1)
final = reverse(arr2, 0, len(arr)-1)
print(final)