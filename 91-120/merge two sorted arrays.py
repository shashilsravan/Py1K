def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[i]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < n1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    print(*arr3)

mergeArrays([1, 3, 5, 7], [2, 4, 6, 8], 4, 4)
