from sys import stdin, stdout

n = 100000
prime = [True] * (n + 1)
prime[0] = prime[1] = False
p = 2
primelist = []
while (p * p < n):
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = False

    p = p + 1

for i in range(2, n + 1):
    if prime[i]:
        primelist.append(i)


def no_of_div(num):
    div = 1
    pid = 0
    p = primelist[pid]
    while p * p <= num:
        if num % p == 0:
            cnt = 0
            while num % p == 0:
                cnt = cnt + 1
                num = num // p
            div = div * (1 + cnt)
        pid = pid + 1
        p = primelist[pid]
    if num > 1:
        div = div * 2
    print(div)


N = int(input())
for z in stdin:
    for num in z.split():
        no_of_div(int(num))
