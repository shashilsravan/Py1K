from sys import stdin, stdout
n = int(stdin.readline())
lis = [int(x) for x in stdin.readline().split()]
temp = sorted(lis)
for t in temp:
    print(lis.index(t), end = " ")