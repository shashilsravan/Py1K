# space complexity : O(n) | time complexity : O(n)
def getNthFib(n):
    memorize = {1: 0, 2: 1}
    if n in memorize:
        # print(memorize)
        return memorize[n]
    else:
        memorize[n] = getNthFib(n - 1) + getNthFib(n - 2)
        # print(memorize)
        return memorize[n]


print(getNthFib(6))