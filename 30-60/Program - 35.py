from collections import Counter
# Contains Duplicate
def containsDuplicate(nums:list):
    # Approach 1
    # dict_ = Counter(nums)
    # lis = dict_.values()
    # for l in lis:
    #     if l>1:
    #         return True
    # return False

    # Approach 2
    # nums = sorted(nums)
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i-1]:
    #         return True
    # return False

    # Approach 3
    return [True, False][len(set(nums)) == len(nums)]


lis_ = [int(x) for x in input().split()]
print(containsDuplicate(lis_))