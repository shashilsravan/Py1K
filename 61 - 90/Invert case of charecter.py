string = input()
a, b = map(int, input().split())
for i in range(len(string)):
    if i == a or i == b:
        print(string[i].swapcase(), end = "")
    else:
        print(string[i], end = "")