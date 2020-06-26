# question asked by uber
# without using divison

lis = [int(x) for x in input().split()]
newlis = []
for i in range(len(lis)):
    temp = lis.copy()
    temp.remove(temp[i])
    product = 1
    for t in temp:
        product *= t
    newlis.append(product)
print(newlis)