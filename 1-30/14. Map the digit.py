from itertools import product
lis = [[''], [''], ['a', 'b', 'c'],  ['d', 'e', 'f'], ['g', 'h', 'i'],
       ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
       ['t','u','v'], ['w', 'x', 'y', 'z']]
num = input() +"1111"
a, b, c = int(num[0]), int(num[1]), int(num[2])
l = list(product(lis[a], lis[b], lis[c]))
for ll in l:
    print("".join(list(ll)), end=" ")
