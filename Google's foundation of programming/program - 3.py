def maxSpan(lis):
    index_dict = {}
    for i, number in enumerate(lis):
        if number not in index_dict:
            index_dict[number] = []
        index_dict[number].append(i)
    max_span = 1

    for ele in index_dict:
        currect = index_dict[ele][-1] - index_dict[ele][0] + 1
        max_span = max(max_span, currect)
    return max_span


print(maxSpan([1, 2, 1, 1, 3]))