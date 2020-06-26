def query(val, lis):
    return True if val in lis else False

lis = []
for _ in range(int(input())):
    a = input().split()
    if a[0] == 'query':
        print(query(a[1], lis))
    elif a[0] == 'add':
        lis.append(a[1])
    elif a[0] == 'remove':
        if a[1] in lis:
            lis.remove(a[1])
    elif a[0] == 'size':
        print(len(lis))

