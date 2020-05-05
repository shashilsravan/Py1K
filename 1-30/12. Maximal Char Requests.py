n = int(input())
string = input()
for _ in range(int(input())):
    a, b = map(int, input().split())
    temp = string[a:b+1].lower()
    print(temp.count(sorted(temp)[-1]))