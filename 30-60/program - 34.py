# Rotate Array
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1
    return nums

def rotate(nums:list, k:int):
    # Approach - 1
    # for i in range(k):
    #     previous = nums[-1]
    #     for j in range(len(nums)):
    #         nums[j], previous = previous, nums[j]

    # Approach 2
    # n = len(nums)
    # a = [-1] * n
    # for i in range(n):
    #     a[(i+k) % n] = nums[i]
    # nums[:] = a
    # print(nums)

    # Approach 3
    nums = reverse(nums, 0, len(nums) - 1)
    nums = reverse(nums, 0, k-1)
    nums = reverse(nums, k, len(nums) - 1)
    print(nums)


num = int(input())
lis = [int(x) for x in input().split()]
rotate(lis, num)