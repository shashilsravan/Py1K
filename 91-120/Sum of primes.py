def SieveOfEratosthenes(number):
    prime = [True for _ in range(number + 1)]
    p = 2
    while p * p <= number:
        if prime[p] == True:
            for i in range(p*2, number + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime[number]
for _ in range(int(input())):
    a, b = map(int, input().split())
    lis = []
    for i in range(a, b+1):
        if SieveOfEratosthenes(i):
            lis.append(i)
    print(sum(lis))