from bisect import bisect
from sys import stdin,stdout
MAX = 1000001
p = 2
prime = [True]*(MAX + 1)
prime[0] = prime[1] = False
primelist = []
while p * p <= MAX:
    if prime[p]:
        for i in range(p*p, MAX+1, p):
            prime[i] = False
    p += 1
for i in range(2, MAX+1):
    if prime[i]:
        primelist.append(i)
for _ in range(int(stdin.readline())):
    num=int(stdin.readline())
    ind = bisect(primelist, num)
    a = num - primelist[ind - 1]
    b = primelist[ind] - num
    if a <= b:
        stdout.write(str(primelist[ind - 1]))
        stdout.write('\n')
    else:
        stdout.write(str(primelist[ind]))
        stdout.write('\n')