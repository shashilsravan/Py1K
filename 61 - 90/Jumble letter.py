from sys import stdin
lis = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y']
for _ in range(int(stdin.readline())):
    string = input()
    for s in string:
        if s not in lis and s.isupper():
            print("."+s.lower(), end = "")
        elif s not in lis and s.islower():
            print("."+s, end = "")
        else:
            pass
    print()