arr = [1,2,3,1,3,1,2,3,2,4,1,2]
k = int(input())
maxsum = 0
for i in range(len(arr) - k):
    maxsum = max(maxsum, sum(arr[i:i+k]))
print(maxsum)