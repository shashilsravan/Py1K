def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [num, potentialMatch]
        else:
            nums[num] = True
    return []


print(twoNumberSum([-4, -1, 1, 3, 5, 6, 8, 11], 13))
