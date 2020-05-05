def bintodec(num):
    print(int(num, 2))


def dectobin(num):
    return bin(num).replace("0b", "")


for _ in range(int(input())):
    a, b, c = input().split()
    b = int(b)
    str1 = str(dectobin(int(a)))
    if len(str1) != 16:
        str1 = "0"*(16 - len(str1)) + str1
    if c == 'L':
        bintodec(str1[b:]+str1[:b])
    elif c == 'R':
        bintodec(str1[len(str1) - b:]+str1[:len(str1) - b])
