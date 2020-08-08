def subArray(array, n, k):
    curr_sum = array[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > k and start < i - 1:
            curr_sum = curr_sum - array[start]
            start += 1
        if curr_sum == k:
            return True
        if i < n:
            curr_sum = curr_sum + array[i]
        i += 1
    return False

print(subArray([3, 1, 1, -6, 1], 5, 0))
