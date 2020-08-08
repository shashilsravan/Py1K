import statistics
from collections import Counter
arr = [1, 4, 2, 3, 2, 1, 3, 3, 4, 2]
# print(statistics.mode(arr))
# print(Counter(arr).most_common(1)[0][0])
print(max(set(arr), key=arr.count))