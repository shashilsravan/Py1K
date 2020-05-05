lis = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for _ in range(int(input())):
    string = input()
    count = 0
    for s in string:
        if s in lis: count += 1
        else: pass
    print(count)