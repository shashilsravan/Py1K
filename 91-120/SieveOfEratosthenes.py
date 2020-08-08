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
    for i in range(number + 1):
        if prime[i]:
            print(i)
#     return prime[number]

SieveOfEratosthenes(10)