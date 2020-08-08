def find_median(array):
    n = len(array)
    if n % 2 == 0:
        median = (array[(n//2)-1] + array[(n//2)])/2
    else:
        median = array[(n//2)]
    return int(median)

n = int(input())
lis = sorted(int(x) for x in input().split())
q2 = find_median(lis)
q1 = find_median(sorted(int(x) for x in lis if x < q2))
q3 = find_median(sorted(int(x) for x in lis if x > q2))
print(q1)
print(q2)
print(q3)