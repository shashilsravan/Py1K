def Equilibrium(arr):
    total_sum = sum(arr)
    l_sum = 0
    for a in arr:
        if l_sum == total_sum - a:
            return True
        else:
            l_sum += a
            total_sum -= a
    return False



arr = [2, 4, 2, -2, 2]
print(Equilibrium(arr))