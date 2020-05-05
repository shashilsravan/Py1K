a, b, c = map(int, input().split())
lis = [int(x) for x in input().split()]
for _ in range(c):
    print(lis[(int(input()) - b)%a])