from sys import stdout, stdin
t = int(stdin.readline())
arr = [int(x) for x in stdin.readline().split()]
arr = [(arr[i], i) for i in range(len(arr))]
arr = sorted(arr, key=lambda x: x[0])
arr = [el[1] - idx for idx, el in enumerate(arr)]
count = max(arr) + 1
stdout.write(str(count))