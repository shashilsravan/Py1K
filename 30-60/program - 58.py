store = {}
arr = [5, 2, 3, 5, 1, 7, 4, 6]
arr.sort()
k = int(input())

left = 0
right = len(arr)-1

while left < right:
    if arr[left] + arr[right] == k:
        print('Yes')
        print(arr[left], arr[right])
        break
    elif arr[left] + arr[right] > k:
        right -= 1
    else:
        left += 1

else:
    print('No')