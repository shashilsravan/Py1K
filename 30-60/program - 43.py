from itertools import combinations
def prime(num):
    if num == 1:
        return False
    count = 2
    while(pow(count, 2) <= num):
        if num % count == 0: return False
        count += 1
    return True

def combination(lis1, lis2):
    for i in range(len(lis1)):
        for j in range(len(lis1)):
            if i != j and prime(int(str(lis1[i]) + str(lis1[j]))) and int(str(lis1[i]) + str(lis1[j])) not in lis2:
                lis2.append(int(str(lis1[i]) + str(lis1[j])))
    return lis2

def primeInRange(a, b):
    lis = []
    for i in range(a, b):
        if prime(i):
            lis.append(i)
    return lis

a, b = map(int, input().split())
lis1 = primeInRange(a, b)

lis2 = combination(lis1, [])
length = len(lis2)
smallest = min(lis2)
largest = max(lis2)
a, b = smallest, largest
i = 0
while i <= length-3:
    a, b = b, a + b
    i += 1
print(b)
# 11 13 17 19
