from collections import defaultdict
# Single number
def singleNumber(nums:list) -> int:
    # Approach 1
    # for n in set(nums):
    #     if nums.count(n) == 1:
    #         return n

    # Approach 2
    # dict_ = defaultdict(int)
    # for n in nums:
    #     dict_[n] += 1
    # for d in dict_:
    #     if dict_[d] == 1:
    #         return d

    # Approach 3
    # return 2 * sum(set(nums)) - sum(nums)

    # Approach 4
    a = 0
    for n in nums:
        a ^= n
    return a